from django.contrib import admin
from .models import (
    Category, Lesson, GlossaryTerm, Quiz, Question, QuizResult,
    Exercise, Device, Protocol, Topology, Cable, VideoLesson, UserProgress
)

# ==================== GOŞMAÇA MAGLUMATLAR (INLINES) ====================
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1
    fields = ['text', 'option_a', 'option_b', 'option_c', 'option_d', 'correct_answer', 'explanation']
    verbose_name = "Sorag"
    verbose_name_plural = "Soraglar"

# ==================== MODEL ADMINLERI ====================
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'order', 'icon']
    list_editable = ['order']          # order list_display-de bar
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'description']

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'difficulty', 'order', 'created_at']
    list_filter = ['category', 'difficulty']
    list_editable = ['order']           # order bar
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'content']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Esasy maglumat', {
            'fields': ('category', 'title', 'slug', 'difficulty', 'order')
        }),
        ('Mazmun', {
            'fields': ('content', 'video_url', 'diagram')
        }),
        ('Sene', {
            'fields': ('created_at', 'updated_at')
        }),
    )

@admin.register(GlossaryTerm)
class GlossaryTermAdmin(admin.ModelAdmin):
    list_display = ['term', 'acronym', 'category']
    list_filter = ['category']
    search_fields = ['term', 'definition', 'acronym']

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'time_limit', 'passing_score']
    list_filter = ['category']
    search_fields = ['title', 'description']
    inlines = [QuestionInline]

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'quiz', 'correct_answer']
    list_filter = ['quiz']
    search_fields = ['text']

@admin.register(QuizResult)
class QuizResultAdmin(admin.ModelAdmin):
    list_display = ['user', 'quiz', 'score', 'total_questions', 'completed_at']
    list_filter = ['quiz', 'completed_at']
    search_fields = ['user__username']
    readonly_fields = ['completed_at']

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'difficulty']
    list_filter = ['category', 'difficulty']
    search_fields = ['title', 'description']

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['name', 'device_type']
    list_filter = ['device_type']
    search_fields = ['name', 'description']

@admin.register(Protocol)
class ProtocolAdmin(admin.ModelAdmin):
    list_display = ['name', 'full_name', 'protocol_type', 'port']
    list_filter = ['protocol_type']
    search_fields = ['name', 'full_name', 'description']

@admin.register(Topology)
class TopologyAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name', 'description']

@admin.register(Cable)
class CableAdmin(admin.ModelAdmin):
    list_display = ['name', 'cable_type', 'max_speed', 'max_distance']
    list_filter = ['cable_type']
    search_fields = ['name', 'description']

@admin.register(VideoLesson)
class VideoLessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'duration', 'order']
    list_filter = ['category']
    list_editable = ['order']           # order bar
    search_fields = ['title', 'description']

@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ['user', 'lesson', 'completed', 'completed_at']
    list_filter = ['completed']
    search_fields = ['user__username', 'lesson__title']
    readonly_fields = ['completed_at']