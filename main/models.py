# models.py - Türkmençe düşündirişli

from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ady")
    slug = models.SlugField(unique=True, verbose_name="Slug")
    description = models.TextField(verbose_name="Düşündiriş")
    icon = models.CharField(max_length=50, help_text="Font Awesome ikonasy", verbose_name="Ikona")
    order = models.IntegerField(default=0, verbose_name="Tertibi")
    
    class Meta:
        verbose_name = "Kategoriýa"
        verbose_name_plural = "Kategoriýalar"
        ordering = ['order']
    
    def __str__(self):
        return self.name

class Lesson(models.Model):
    DIFFICULTY_CHOICES = [
        ('beginner', 'Başlangyç'),
        ('intermediate', 'Orta'),
        ('advanced', 'Ýokary'),
    ]
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='lessons', verbose_name="Kategoriýa")
    title = models.CharField(max_length=200, verbose_name="Ady")
    slug = models.SlugField(unique=True, verbose_name="Slug")
    content = models.TextField(verbose_name="Mazmuny")
    video_url = models.URLField(blank=True, null=True, verbose_name="Wideo URL")
    diagram = models.ImageField(upload_to='diagrams/', blank=True, null=True, verbose_name="Diagramma")
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES, default='beginner', verbose_name="Kynlylyk")
    order = models.IntegerField(default=0, verbose_name="Tertibi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Döredilen wagty")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Üýtgedilen wagty")
    
    class Meta:
        verbose_name = "Ders"
        verbose_name_plural = "Dersler"
        ordering = ['category', 'order']
    
    def __str__(self):
        return f"{self.category.name} - {self.title}"

class GlossaryTerm(models.Model):
    term = models.CharField(max_length=100, unique=True, verbose_name="Termin")
    definition = models.TextField(verbose_name="Kesgitlemesi")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Kategoriýa")
    example = models.TextField(blank=True, verbose_name="Mysal")
    acronym = models.CharField(max_length=20, blank=True, verbose_name="Gysgaltmasy")
    
    class Meta:
        verbose_name = "Sözlük termini"
        verbose_name_plural = "Sözlük terminleri"
        ordering = ['term']
    
    def __str__(self):
        return self.term

class Quiz(models.Model):
    title = models.CharField(max_length=200, verbose_name="Ady")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='quizzes', verbose_name="Kategoriýa")
    description = models.TextField(blank=True, verbose_name="Düşündiriş")
    time_limit = models.IntegerField(help_text="Minut bilen", default=10, verbose_name="Wagt çäklendirmesi")
    passing_score = models.IntegerField(default=70, verbose_name="Geçiş baly")
    
    class Meta:
        verbose_name = "Test"
        verbose_name_plural = "Testler"
    
    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions', verbose_name="Test")
    text = models.TextField(verbose_name="Sorag")
    option_a = models.CharField(max_length=200, verbose_name="Jogap A")
    option_b = models.CharField(max_length=200, verbose_name="Jogap B")
    option_c = models.CharField(max_length=200, verbose_name="Jogap C")
    option_d = models.CharField(max_length=200, verbose_name="Jogap D")
    correct_answer = models.CharField(max_length=1, choices=[
        ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')
    ], verbose_name="Dogry jogap")
    explanation = models.TextField(blank=True, verbose_name="Düşündiriş")
    
    class Meta:
        verbose_name = "Sorag"
        verbose_name_plural = "Soraglar"
    
    def __str__(self):
        return f"{self.quiz.title} - {self.text[:50]}"

class QuizResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Ulanyjy")
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, verbose_name="Test")
    score = models.IntegerField(verbose_name="Baly")
    total_questions = models.IntegerField(verbose_name="Sorag sany")
    completed_at = models.DateTimeField(auto_now_add=True, verbose_name="Tamamlanan wagty")
    
    class Meta:
        verbose_name = "Test netijesi"
        verbose_name_plural = "Test netijeleri"
    
    def __str__(self):
        return f"{self.user} - {self.quiz.title} - {self.score}%"

class Exercise(models.Model):
    title = models.CharField(max_length=200, verbose_name="Ady")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='exercises', verbose_name="Kategoriýa")
    description = models.TextField(verbose_name="Düşündiriş")
    initial_config = models.TextField(help_text="Başlangyç konfigurasiýa", blank=True, verbose_name="Başlangyç konfig")
    solution = models.TextField(help_text="Dogry çözgüt", verbose_name="Çözgüt")
    difficulty = models.CharField(max_length=20, choices=Lesson.DIFFICULTY_CHOICES, verbose_name="Kynlylyk")
    hint = models.TextField(blank=True, verbose_name="Maslahat")
    
    class Meta:
        verbose_name = "Maşk"
        verbose_name_plural = "Maşklar"
    
    def __str__(self):
        return self.title

class Device(models.Model):
    DEVICE_TYPES = [
        ('router', 'Router'),
        ('switch', 'Switch'),
        ('hub', 'Hub'),
        ('firewall', 'Firewall'),
        ('access_point', 'Access Point'),
        ('modem', 'Modem'),
        ('repeater', 'Repeater'),
        ('bridge', 'Bridge'),
    ]
    
    name = models.CharField(max_length=100, verbose_name="Ady")
    device_type = models.CharField(max_length=20, choices=DEVICE_TYPES, verbose_name="Enjam görnüşi")
    description = models.TextField(verbose_name="Düşündiriş")
    image = models.ImageField(upload_to='devices/', blank=True, null=True, verbose_name="Suraty")
    function = models.TextField(verbose_name="Wezipesi")
    advantages = models.TextField(verbose_name="Ýokluklary")
    disadvantages = models.TextField(verbose_name="Gowsuzlyklary")
    
    class Meta:
        verbose_name = "Enjam"
        verbose_name_plural = "Enjamlar"
    
    def __str__(self):
        return f"{self.get_device_type_display()} - {self.name}"

class Protocol(models.Model):
    PROTOCOL_TYPES = [
        ('application', 'Amaly gatlak'),
        ('transport', 'Ulag gatlagy'),
        ('internet', 'Internet gatlagy'),
        ('network_access', 'Ulgama giriş'),
    ]
    
    name = models.CharField(max_length=50, verbose_name="Ady")
    full_name = models.CharField(max_length=100, verbose_name="Doly ady")
    protocol_type = models.CharField(max_length=20, choices=PROTOCOL_TYPES, verbose_name="Gatlak")
    port = models.IntegerField(null=True, blank=True, verbose_name="Port")
    description = models.TextField(verbose_name="Düşündiriş")
    uses = models.TextField(verbose_name="Ulanylyşy")
    example = models.TextField(blank=True, verbose_name="Mysal")
    
    class Meta:
        verbose_name = "Protokol"
        verbose_name_plural = "Protokollar"
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Topology(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ady")
    description = models.TextField(verbose_name="Düşündiriş")
    diagram = models.ImageField(upload_to='topologies/', verbose_name="Diagramma")
    advantages = models.TextField(verbose_name="Ýokluklary")
    disadvantages = models.TextField(verbose_name="Gowsuzlyklary")
    use_cases = models.TextField(verbose_name="Ulanylyş ýagdaýlary")
    
    class Meta:
        verbose_name = "Topologiýa"
        verbose_name_plural = "Topologiýalar"
    
    def __str__(self):
        return self.name

class Cable(models.Model):
    CABLE_TYPES = [
        ('ethernet', 'Ethernet'),
        ('fiber', 'Fiber Optik'),
        ('coaxial', 'Koaksial'),
        ('serial', 'Serial'),
        ('console', 'Console'),
        ('usb', 'USB'),
    ]
    
    name = models.CharField(max_length=100, verbose_name="Ady")
    cable_type = models.CharField(max_length=20, choices=CABLE_TYPES, verbose_name="Kabel görnüşi")
    description = models.TextField(verbose_name="Düşündiriş")
    max_speed = models.CharField(max_length=50, verbose_name="Iň ýokary tizlik")
    max_distance = models.CharField(max_length=50, verbose_name="Iň ýokary aralyk")
    connector_type = models.CharField(max_length=50, verbose_name="Konnektor görnüşi")
    image = models.ImageField(upload_to='cables/', blank=True, null=True, verbose_name="Suraty")
    
    class Meta:
        verbose_name = "Kabel"
        verbose_name_plural = "Kabeller"
    
    def __str__(self):
        return self.name

class VideoLesson(models.Model):
    title = models.CharField(max_length=200, verbose_name="Ady")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='videos', verbose_name="Kategoriýa")
    youtube_id = models.CharField(max_length=50, help_text="YouTube video ID", verbose_name="YouTube ID")
    duration = models.CharField(max_length=20, help_text="Mysal: 15:30", verbose_name="Dowamlylygy")
    description = models.TextField(verbose_name="Düşündiriş")
    order = models.IntegerField(default=0, verbose_name="Tertibi")
    
    class Meta:
        verbose_name = "Wideo ders"
        verbose_name_plural = "Wideo dersler"
        ordering = ['category', 'order']
    
    def __str__(self):
        return self.title

class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Ulanyjy")
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name="Ders")
    completed = models.BooleanField(default=False, verbose_name="Tamamlandy")
    completed_at = models.DateTimeField(null=True, blank=True, verbose_name="Tamamlanan wagty")
    
    class Meta:
        verbose_name = "Ulanyjy progressi"
        verbose_name_plural = "Ulanyjy progressleri"
        unique_together = ['user', 'lesson']
    
    def __str__(self):
        return f"{self.user} - {self.lesson.title} - {'Tamamlandy' if self.completed else 'Dowam edýär'}"