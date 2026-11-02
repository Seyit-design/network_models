from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import *
import random
import ipaddress
import subprocess
import platform
import socket
import re

# ==================== ESAZY SAHYPA ====================
def index(request):
    categories = Category.objects.all()[:6]
    recent_lessons = Lesson.objects.order_by('-created_at')[:5]
    random_quiz = Quiz.objects.order_by('?').first()
    context = {
        'categories': categories,
        'recent_lessons': recent_lessons,
        'random_quiz': random_quiz,
    }
    return render(request, 'main/index.html', context)

@login_required
def dashboard(request):
    user_progress = UserProgress.objects.filter(user=request.user)
    completed_lessons = user_progress.filter(completed=True).count()
    total_lessons = Lesson.objects.count()
    quiz_results = QuizResult.objects.filter(user=request.user).order_by('-completed_at')[:5]
    context = {
        'completed_lessons': completed_lessons,
        'total_lessons': total_lessons,
        'progress_percentage': (completed_lessons / total_lessons * 100) if total_lessons > 0 else 0,
        'quiz_results': quiz_results,
    }
    return render(request, 'main/dashboard.html', context)

# ==================== KATEGORIÝALAR ====================
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'main/categories/list.html', {'categories': categories})

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    lessons = category.lessons.all()
    quizzes = category.quizzes.all()
    exercises = category.exercises.all()
    context = {
        'category': category,
        'lessons': lessons,
        'quizzes': quizzes,
        'exercises': exercises,
    }
    return render(request, 'main/categories/detail.html', context)

# ==================== OSI MODEL ====================
def osi_index(request):
    layers = [
        {'number': 1, 'name': 'Fiziki gatlak', 'description': 'Kabel, signal, elektrik impulslary'},
        {'number': 2, 'name': 'Maglumat baglanyşyk gatlagy', 'description': 'MAC adresler, switçler'},
        {'number': 3, 'name': 'Ulgam gatlagy', 'description': 'IP adresler, routerler'},
        {'number': 4, 'name': 'Ulag gatlagy', 'description': 'TCP, UDP, port nomerleri'},
        {'number': 5, 'name': 'Sessiýa gatlagy', 'description': 'Sessiýa dolandyryş'},
        {'number': 6, 'name': 'Prezentasiýa gatlagy', 'description': 'Şifrleme, kompressiýa'},
        {'number': 7, 'name': 'Amaly gatlak', 'description': 'HTTP, FTP, SMTP'},
    ]
    return render(request, 'main/osi/index.html', {'layers': layers})

def osi_layer_detail(request, layer):
    layers = {
        1: {'name': 'Fiziki gatlak', 'function': 'Bitleri fiziki signala öwürmek', 'devices': ['Hub', 'Repeater', 'Kabel'], 'protocols': ['Ethernet', 'USB']},
        2: {'name': 'Maglumat baglanyşyk gatlagy', 'function': 'Fiziki adresleme, ýalňyşlyklary tapmak', 'devices': ['Switch', 'Bridge'], 'protocols': ['MAC', 'LLC']},
        3: {'name': 'Ulgam gatlagy', 'function': 'Marşrutizasiýa, mantykly adresleme', 'devices': ['Router'], 'protocols': ['IP', 'ICMP']},
        4: {'name': 'Ulag gatlagy', 'function': 'Ulag hyzmatlary, akym dolandyryş', 'devices': [], 'protocols': ['TCP', 'UDP']},
        5: {'name': 'Sessiýa gatlagy', 'function': 'Sessiýa dolandyryş, sinhronizasiýa', 'devices': [], 'protocols': ['NetBIOS', 'RPC']},
        6: {'name': 'Prezentasiýa gatlagy', 'function': 'Maglumat formatirleme, şifrleme', 'devices': [], 'protocols': ['SSL', 'TLS']},
        7: {'name': 'Amaly gatlak', 'function': 'Ulanyjy programmalary bilen aragatnaşyk', 'devices': [], 'protocols': ['HTTP', 'FTP', 'SMTP']},
    }
    layer_info = layers.get(layer, layers[1])
    return render(request, 'main/osi/layer_detail.html', {'layer': layer_info, 'layer_num': layer})

def osi_layer1(request):
    return render(request, 'main/osi/layer1.html', {'layer': 'Fiziki gatlak'})
def osi_layer2(request):
    return render(request, 'main/osi/layer2.html', {'layer': 'Maglumat baglanyşyk gatlagy'})
def osi_layer3(request):
    return render(request, 'main/osi/layer3.html', {'layer': 'Ulgam gatlagy'})
def osi_layer4(request):
    return render(request, 'main/osi/layer4.html', {'layer': 'Ulag gatlagy'})
def osi_layer5(request):
    return render(request, 'main/osi/layer5.html', {'layer': 'Sessiýa gatlagy'})
def osi_layer6(request):
    return render(request, 'main/osi/layer6.html', {'layer': 'Prezentasiýa gatlagy'})
def osi_layer7(request):
    return render(request, 'main/osi/layer7.html', {'layer': 'Amaly gatlak'})

# ==================== TCP/IP MODEL ====================
def tcpip_index(request):
    layers = [
        {'number': 1, 'name': 'Ulgama giriş gatlagy', 'description': 'Fiziki we maglumat baglanyşyk'},
        {'number': 2, 'name': 'Internet gatlagy', 'description': 'IP, ICMP, ARP'},
        {'number': 3, 'name': 'Ulag gatlagy', 'description': 'TCP, UDP'},
        {'number': 4, 'name': 'Amaly gatlak', 'description': 'HTTP, FTP, DNS, SMTP'},
    ]
    return render(request, 'main/tcpip/index.html', {'layers': layers})

def tcpip_layer_detail(request, layer):
    layers = {
        1: {'name': 'Ulgama giriş gatlagy', 'function': 'Fiziki we maglumat baglanyşyk', 'protocols': ['Ethernet', 'ARP'], 'devices': ['Hub', 'Switch']},
        2: {'name': 'Internet gatlagy', 'function': 'IP adresleme we marşrutizasiýa', 'protocols': ['IP', 'ICMP'], 'devices': ['Router']},
        3: {'name': 'Ulag gatlagy', 'function': 'Ulag hyzmatlary', 'protocols': ['TCP', 'UDP'], 'devices': []},
        4: {'name': 'Amaly gatlak', 'function': 'Programmalar üçin hyzmatlar', 'protocols': ['HTTP', 'FTP', 'SMTP', 'DNS'], 'devices': []},
    }
    layer_info = layers.get(layer, layers[1])
    return render(request, 'main/tcpip/layer_detail.html', {'layer': layer_info, 'layer_num': layer})

def tcpip_layer1(request):
    return render(request, 'main/tcpip/layer1.html', {'layer': 'Ulgama giriş gatlagy'})
def tcpip_layer2(request):
    return render(request, 'main/tcpip/layer2.html', {'layer': 'Internet gatlagy'})
def tcpip_layer3(request):
    return render(request, 'main/tcpip/layer3.html', {'layer': 'Ulag gatlagy'})
def tcpip_layer4(request):
    return render(request, 'main/tcpip/layer4.html', {'layer': 'Amaly gatlak'})
def tcpip_layer5(request):
    return render(request, 'main/tcpip/layer5.html', {'layer': 'Fiziki we maglumat baglanyşyk'})

# ==================== ESASY TOR DÜŞÜNJELERI ====================
def basic_index(request):
    return render(request, 'main/basic/index.html')
def basic_ip(request):
    return render(request, 'main/basic/ip.html')
def basic_ip_classes(request):
    return render(request, 'main/basic/ip_classes.html')
def basic_mac(request):
    return render(request, 'main/basic/mac.html')
def basic_subnetting(request):
    return render(request, 'main/basic/subnetting.html')
def basic_vlan(request):
    return render(request, 'main/basic/vlan.html')
def basic_nat(request):
    return render(request, 'main/basic/nat.html')
def basic_public_private(request):
    return render(request, 'main/basic/public_private.html')

# ==================== TOR ENJAMLARY ====================
def devices_index(request):
    return render(request, 'main/devices/index.html')
def device_router(request):
    return render(request, 'main/devices/router.html')
def device_switch(request):
    return render(request, 'main/devices/switch.html')
def device_hub(request):
    return render(request, 'main/devices/hub.html')
def device_firewall(request):
    return render(request, 'main/devices/firewall.html')
def device_ap(request):
    return render(request, 'main/devices/access_point.html')
def device_modem(request):
    return render(request, 'main/devices/modem.html')
def device_repeater(request):
    return render(request, 'main/devices/repeater.html')
def device_bridge(request):
    return render(request, 'main/devices/bridge.html')
def device_gateway(request):
    return render(request, 'main/devices/gateway.html')
def device_comparison(request):
    return render(request, 'main/devices/comparison.html')

# ==================== PROTOKOLLAR ====================
def protocols_index(request):
    return render(request, 'main/protocols/index.html')
def protocol_tcp(request):
    return render(request, 'main/protocols/tcp.html')
def protocol_udp(request):
    return render(request, 'main/protocols/udp.html')
def protocol_ip(request):
    return render(request, 'main/protocols/ip.html')
def protocol_icmp(request):
    return render(request, 'main/protocols/icmp.html')
def protocol_arp(request):
    return render(request, 'main/protocols/arp.html')
def protocol_dhcp(request):
    return render(request, 'main/protocols/dhcp.html')
def protocol_dns(request):
    return render(request, 'main/protocols/dns.html')
def protocol_http(request):
    return render(request, 'main/protocols/http.html')
def protocol_https(request):
    return render(request, 'main/protocols/https.html')
def protocol_ftp(request):
    return render(request, 'main/protocols/ftp.html')
def protocol_smtp(request):
    return render(request, 'main/protocols/smtp.html')
def protocol_pop3(request):
    return render(request, 'main/protocols/pop3.html')
def protocol_imap(request):
    return render(request, 'main/protocols/imap.html')
def protocol_ssh(request):
    return render(request, 'main/protocols/ssh.html')
def protocol_telnet(request):
    return render(request, 'main/protocols/telnet.html')
def protocol_snmp(request):
    return render(request, 'main/protocols/snmp.html')
def protocol_comparison(request):
    return render(request, 'main/protocols/comparison.html')
def protocol_ports(request):
    common_ports = [
        {'port': 20, 'protocol': 'FTP-data', 'description': 'Faýl transferi - maglumat'},
        {'port': 21, 'protocol': 'FTP', 'description': 'Faýl transferi - dolandyryş'},
        {'port': 22, 'protocol': 'SSH', 'description': 'Howply shell'},
        {'port': 23, 'protocol': 'Telnet', 'description': 'Uzakyňdan dolandyryş'},
        {'port': 25, 'protocol': 'SMTP', 'description': 'Email ibermek'},
        {'port': 53, 'protocol': 'DNS', 'description': 'Domain atlar ulgamy'},
        {'port': 80, 'protocol': 'HTTP', 'description': 'Web trafigi'},
        {'port': 110, 'protocol': 'POP3', 'description': 'Email almak'},
        {'port': 143, 'protocol': 'IMAP', 'description': 'Email almak'},
        {'port': 443, 'protocol': 'HTTPS', 'description': 'Howply web trafigi'},
    ]
    return render(request, 'main/protocols/ports.html', {'ports': common_ports})

# ==================== KABELLER WE BIRIKMELER ====================
def cables_index(request):
    return render(request, 'main/cables/index.html')
def cable_ethernet(request):
    return render(request, 'main/cables/ethernet.html')
def cable_cat5(request):
    return render(request, 'main/cables/cat5.html')
def cable_cat5e(request):
    return render(request, 'main/cables/cat5e.html')
def cable_cat6(request):
    return render(request, 'main/cables/cat6.html')
def cable_cat7(request):
    return render(request, 'main/cables/cat7.html')
def cable_fiber(request):
    return render(request, 'main/cables/fiber.html')
def fiber_single_mode(request):
    return render(request, 'main/cables/single_mode.html')
def fiber_multi_mode(request):
    return render(request, 'main/cables/multi_mode.html')
def cable_coaxial(request):
    return render(request, 'main/cables/coaxial.html')
def cable_serial(request):
    return render(request, 'main/cables/serial.html')
def cable_console(request):
    return render(request, 'main/cables/console.html')
def cable_usb(request):
    return render(request, 'main/cables/usb.html')
def wireless_index(request):
    return render(request, 'main/cables/wireless/index.html')
def wireless_wifi(request):
    return render(request, 'main/cables/wireless/wifi.html')
def wireless_bluetooth(request):
    return render(request, 'main/cables/wireless/bluetooth.html')
def wireless_cellular(request):
    return render(request, 'main/cables/wireless/cellular.html')
def cable_crimping(request):
    return render(request, 'main/cables/crimping.html')
def cable_colors(request):
    color_codes = {
        'T568A': ['AÝ - Ak ýaşyl', 'Ý - Ýaşyl', 'AÝ - Ak ýaşyl', 'G - Gök', 'AG - Ak gök', 'Ý - Ýaşyl', 'AM - Ak goňur', 'M - Goňur'],
        'T568B': ['AÝ - Ak ýaşyl', 'Ý - Ýaşyl', 'AÝ - Ak ýaşyl', 'G - Gök', 'AG - Ak gök', 'Ý - Ýaşyl', 'AM - Ak goňur', 'M - Goňur'],
    }
    return render(request, 'main/cables/colors.html', {'color_codes': color_codes})

# ==================== TOPOLOGIÝALAR ====================
def topologies_index(request):
    return render(request, 'main/topologies/index.html')
def topology_star(request):
    return render(request, 'main/topologies/star.html')
def topology_bus(request):
    return render(request, 'main/topologies/bus.html')
def topology_ring(request):
    return render(request, 'main/topologies/ring.html')
def topology_mesh(request):
    return render(request, 'main/topologies/mesh.html')
def topology_tree(request):
    return render(request, 'main/topologies/tree.html')
def topology_hybrid(request):
    return render(request, 'main/topologies/hybrid.html')
def topology_daisy(request):
    return render(request, 'main/topologies/daisy.html')
def topology_comparison(request):
    return render(request, 'main/topologies/comparison.html')

# ==================== GURALLAR (TOOLS) ====================
# (Bu bölüm eýýäm bar, ýöne bir ýerde goşýarys)
def tools_index(request):
    return render(request, 'main/tools/index.html')

def ip_calculator(request):
    return render(request, 'main/tools/ip_calculator.html')

def ip_calculator_result(request):
    if request.method == 'POST':
        ip_address = request.POST.get('ip_address')
        subnet_mask = request.POST.get('subnet_mask')
        try:
            network = ipaddress.IPv4Network(f'{ip_address}/{subnet_mask}', strict=False)
            hosts = list(network.hosts())
            result = {
                'network_address': str(network.network_address),
                'broadcast_address': str(network.broadcast_address),
                'netmask': str(network.netmask),
                'wildcard': str(network.hostmask),
                'num_hosts': network.num_addresses - 2,
                'first_host': str(hosts[0]) if hosts else 'None',
                'last_host': str(hosts[-1]) if hosts else 'None',
                'binary_network': '.'.join([format(int(x), '08b') for x in str(network.network_address).split('.')]),
                'binary_mask': '.'.join([format(int(x), '08b') for x in str(network.netmask).split('.')]),
            }
        except Exception as e:
            result = {'error': f'Nädogry IP ýa-da subnet mask: {str(e)}'}
        return render(request, 'main/tools/ip_calculator_result.html', {'result': result})
    return redirect('ip_calculator')

def subnet_calculator(request):
    return render(request, 'main/tools/subnet_calculator.html')

def subnet_calculator_result(request):
    if request.method == 'POST':
        ip_address = request.POST.get('ip_address')
        prefix = request.POST.get('prefix')
        num_subnets = int(request.POST.get('num_subnets', 4))
        try:
            network = ipaddress.IPv4Network(f'{ip_address}/{prefix}', strict=False)
            new_prefix = network.prefixlen + (num_subnets.bit_length() - 1)
            subnets = list(network.subnets(new_prefix=new_prefix))
            results = []
            for i, subnet in enumerate(subnets[:num_subnets]):
                hosts = list(subnet.hosts())
                results.append({
                    'subnet': i + 1,
                    'network': str(subnet.network_address),
                    'netmask': str(subnet.netmask),
                    'first_host': str(hosts[0]) if hosts else 'None',
                    'last_host': str(hosts[-1]) if hosts else 'None',
                    'broadcast': str(subnet.broadcast_address),
                    'hosts': subnet.num_addresses - 2,
                    'cidr': f"/{subnet.prefixlen}",
                })
        except Exception as e:
            results = {'error': str(e)}
        return render(request, 'main/tools/subnet_calculator_result.html', {'results': results, 'original': ip_address})
    return redirect('subnet_calculator')

def vlsm_calculator(request):
    if request.method == 'POST':
        # Implement VLSM logic here if needed
        return render(request, 'main/tools/vlsm_calculator_result.html')
    return render(request, 'main/tools/vlsm_calculator.html')

def mac_converter(request):
    result = None
    if request.method == 'POST':
        mac = request.POST.get('mac', '').strip()
        mac_clean = re.sub(r'[^a-fA-F0-9]', '', mac)
        if len(mac_clean) == 12:
            formats = {
                'cisco': '.'.join([mac_clean[i:i+4] for i in range(0, 12, 4)]),
                'linux': ':'.join([mac_clean[i:i+2] for i in range(0, 12, 2)]),
                'windows': '-'.join([mac_clean[i:i+2] for i in range(0, 12, 2)]),
                'bare': mac_clean,
                'vendor': mac_clean[:6].upper(),
            }
            result = formats
        else:
            result = {'error': 'Nädogry MAC adres (12 simwol bolmaly)'}
    return render(request, 'main/tools/mac_converter.html', {'result': result})

def binary_converter(request):
    result = None
    if request.method == 'POST':
        number = request.POST.get('number', '').strip()
        direction = request.POST.get('direction')
        try:
            if direction == 'to_binary':
                dec_num = int(number)
                result = {'original': number, 'converted': bin(dec_num)[2:], 'type': 'decimal_to_binary'}
            else:
                result = {'original': number, 'converted': str(int(number, 2)), 'type': 'binary_to_decimal'}
        except ValueError:
            result = {'error': 'Nädogry san formaty'}
    return render(request, 'main/tools/binary_converter.html', {'result': result})

def hex_converter(request):
    result = None
    if request.method == 'POST':
        number = request.POST.get('number', '').strip()
        direction = request.POST.get('direction')
        try:
            if direction == 'to_hex':
                dec_num = int(number)
                result = {'original': number, 'converted': hex(dec_num)[2:].upper(), 'type': 'decimal_to_hex'}
            else:
                result = {'original': number, 'converted': str(int(number, 16)), 'type': 'hex_to_decimal'}
        except ValueError:
            result = {'error': 'Nädogry san formaty'}
    return render(request, 'main/tools/hex_converter.html', {'result': result})

def port_scanner(request):
    result = None
    if request.method == 'POST':
        host = request.POST.get('host', '').strip()
        start_port = int(request.POST.get('start_port', 1))
        end_port = int(request.POST.get('end_port', 1024))
        open_ports = []
        try:
            target_ip = socket.gethostbyname(host)
            for port in range(start_port, min(end_port, start_port+20)):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.5)
                if sock.connect_ex((target_ip, port)) == 0:
                    open_ports.append(port)
                sock.close()
            result = {'host': host, 'ip': target_ip, 'open_ports': open_ports, 'port_range': f"{start_port}-{end_port}"}
        except Exception as e:
            result = {'error': str(e)}
    return render(request, 'main/tools/port_scanner.html', {'result': result})

def ping_test(request):
    result = None
    if request.method == 'POST':
        host = request.POST.get('host', '').strip()
        try:
            param = '-n' if platform.system().lower() == 'windows' else '-c'
            command = ['ping', param, '4', host]
            output = subprocess.run(command, capture_output=True, text=True, timeout=10)
            result = {'host': host, 'output': output.stdout + output.stderr, 'success': output.returncode == 0}
        except Exception as e:
            result = {'error': str(e), 'host': host}
    return render(request, 'main/tools/ping_test.html', {'result': result})

def traceroute(request):
    result = None
    if request.method == 'POST':
        host = request.POST.get('host', '').strip()
        try:
            if platform.system().lower() == 'windows':
                command = ['tracert', '-h', '10', host]
            else:
                command = ['traceroute', '-m', '10', host]
            output = subprocess.run(command, capture_output=True, text=True, timeout=30)
            result = {'host': host, 'output': output.stdout + output.stderr}
        except Exception as e:
            result = {'error': str(e), 'host': host}
    return render(request, 'main/tools/traceroute.html', {'result': result})

def mac_finder(request):
    result = None
    if request.method == 'POST':
        mac = request.POST.get('mac', '').strip()
        mac_clean = re.sub(r'[^a-fA-F0-9]', '', mac)
        if len(mac_clean) >= 6:
            oui = mac_clean[:6].upper()
            vendors = {
                '00037F': 'Atheros', '001377': 'Samsung', '0050F2': 'Microsoft',
                '00A0C9': 'Intel', '08002B': 'DEC', '3C970E': 'Hewlett Packard',
                'AC853D': 'LG Electronics', 'BC305B': 'Dell', 'F8E0F9': 'Sony',
                '54E6FC': 'Apple', '60F81D': 'Xerox', '000000': 'Broadcast',
            }
            vendor = vendors.get(oui, 'Belli däl')
            result = {'mac': mac, 'oui': oui, 'vendor': vendor}
        else:
            result = {'error': 'MAC adres 6 simwoldan az'}
    return render(request, 'main/tools/mac_finder.html', {'result': result})

def wildcard_calculator(request):
    result = None
    if request.method == 'POST':
        subnet_mask = request.POST.get('subnet_mask', '').strip()
        try:
            mask_parts = subnet_mask.split('.')
            wildcard_parts = [str(255 - int(part)) for part in mask_parts]
            wildcard = '.'.join(wildcard_parts)
            result = {
                'subnet_mask': subnet_mask,
                'wildcard': wildcard,
                'binary_subnet': '.'.join([format(int(x), '08b') for x in mask_parts]),
                'binary_wildcard': '.'.join([format(int(x), '08b') for x in wildcard_parts]),
            }
        except Exception as e:
            result = {'error': str(e)}
    return render(request, 'main/tools/wildcard_calculator.html', {'result': result})

# ==================== AMALY MAŞKLAR ====================
def exercises_index(request):
    return render(request, 'main/exercises/index.html')
def ex_subnetting(request):
    return render(request, 'main/exercises/subnetting/index.html')
def ex_subnetting_basic(request):
    return render(request, 'main/exercises/subnetting/basic.html')
def ex_subnetting_intermediate(request):
    return render(request, 'main/exercises/subnetting/intermediate.html')
def ex_subnetting_advanced(request):
    return render(request, 'main/exercises/subnetting/advanced.html')
def ex_ip_classes(request):
    return render(request, 'main/exercises/ip_classes.html')
def ex_vlsm(request):
    return render(request, 'main/exercises/vlsm.html')
def ex_cabling(request):
    return render(request, 'main/exercises/cabling.html')
def ex_routing(request):
    return render(request, 'main/exercises/routing.html')
def ex_subnetting_check(request):
    if request.method == 'POST':
        user_answer = request.POST.get('answer')
        correct_answer = request.POST.get('correct_answer')
        is_correct = (user_answer == correct_answer)
        return JsonResponse({'correct': is_correct, 'message': 'Dogry!' if is_correct else 'Ýalňyş! Gaýtadan synanyşyň.'})
    return JsonResponse({'error': 'Method not allowed'})

# ==================== INTERAKTIW OÝUNLAR ====================
def games_index(request):
    return render(request, 'main/games/index.html')
def game_layer_quiz(request):
    return render(request, 'main/games/layer_quiz.html')
def game_layer_quiz_check(request):
    # Simple check for demo
    if request.method == 'POST':
        answers = request.POST.dict()
        correct_count = 0
        total = 0
        for key, value in answers.items():
            if key == 'csrfmiddlewaretoken':
                continue
            total += 1
            # Example: if key == 'layer1' and value == '7' then correct
            if key == 'layer1' and value == '7':
                correct_count += 1
        score = (correct_count / total * 100) if total > 0 else 0
        return JsonResponse({'score': score, 'correct': correct_count, 'total': total})
    return JsonResponse({'error': 'Method not allowed'})
def game_protocol_match(request):
    return render(request, 'main/games/protocol_match.html')
def game_drag_drop(request):
    return render(request, 'main/games/drag_drop.html')
def game_ip_game(request):
    return render(request, 'main/games/ip_game.html')
def game_memory(request):
    return render(request, 'main/games/memory.html')

# ==================== WIDEO DERSLER ====================
def videos_index(request):
    return render(request, 'main/videos/index.html')
def video_osi(request):
    return render(request, 'main/videos/osi.html')
def video_tcpip(request):
    return render(request, 'main/videos/tcpip.html')
def video_routing(request):
    return render(request, 'main/videos/routing.html')
def video_switching(request):
    return render(request, 'main/videos/switching.html')
def video_subnetting(request):
    return render(request, 'main/videos/subnetting.html')
def video_detail(request, video_id):
    # video = get_object_or_404(VideoLesson, id=video_id)
    return render(request, 'main/videos/detail.html', {'video_id': video_id})

# ==================== TESTLER ====================
def quiz_index(request):
    return render(request, 'main/quiz/index.html')
def quiz_osi(request):
    return redirect('quiz_detail', quiz_id=1)  # assume quiz with id=1 exists
def quiz_tcpip(request):
    return redirect('quiz_detail', quiz_id=2)
def quiz_protocols(request):
    return redirect('quiz_detail', quiz_id=3)
def quiz_devices(request):
    return redirect('quiz_detail', quiz_id=4)
def quiz_ip(request):
    return redirect('quiz_detail', quiz_id=5)
def quiz_detail(request, quiz_id):
    # quiz = get_object_or_404(Quiz, id=quiz_id)
    # questions = quiz.questions.all()
    return render(request, 'main/quiz/detail.html', {'quiz_id': quiz_id})
def quiz_submit(request, quiz_id):
    if request.method == 'POST':
        # Process answers
        return redirect('quiz_result', result_id=1)
    return redirect('quiz_detail', quiz_id=quiz_id)
def quiz_result(request, result_id):
    # result = get_object_or_404(QuizResult, id=result_id)
    return render(request, 'main/quiz/result.html', {'result_id': result_id})
def quiz_leaderboard(request):
    # top_results = QuizResult.objects.order_by('-score')[:20]
    return render(request, 'main/quiz/leaderboard.html')

# ==================== SÖZLÜK ====================
def glossary_index(request):
    # terms = GlossaryTerm.objects.all()[:50]
    return render(request, 'main/glossary/index.html')
def glossary_search(request):
    query = request.GET.get('q', '')
    # terms = GlossaryTerm.objects.filter(Q(term__icontains=query) | Q(definition__icontains=query)) if query else []
    return render(request, 'main/glossary/search.html', {'query': query})
def glossary_detail(request, term):
    # term_obj = get_object_or_404(GlossaryTerm, term__iexact=term)
    return render(request, 'main/glossary/detail.html', {'term': term})
def glossary_by_letter(request, letter):
    # terms = GlossaryTerm.objects.filter(term__istartswith=letter)
    return render(request, 'main/glossary/by_letter.html', {'letter': letter})

# ==================== LABORATORIÝALAR ====================
def labs_index(request):
    return render(request, 'main/labs/index.html')
def lab_packet_tracer(request):
    return render(request, 'main/labs/packet_tracer.html')
def lab_cisco_commands(request):
    return render(request, 'main/labs/cisco_commands.html')
def lab_simulation(request):
    return render(request, 'main/labs/simulation.html')
def lab_basic_config(request):
    return render(request, 'main/labs/basic_config.html')
def lab_vlan_config(request):
    return render(request, 'main/labs/vlan_config.html')
def lab_routing_config(request):
    return render(request, 'main/labs/routing_config.html')

# ==================== TROUBLESHOOTING ====================
def troubleshoot_index(request):
    return render(request, 'main/troubleshoot/index.html')
def tshoot_connectivity(request):
    return render(request, 'main/troubleshoot/connectivity.html')
def tshoot_dns(request):
    return render(request, 'main/troubleshoot/dns.html')
def tshoot_ip_conflict(request):
    return render(request, 'main/troubleshoot/ip_conflict.html')
def tshoot_performance(request):
    return render(request, 'main/troubleshoot/performance.html')
def tshoot_security(request):
    return render(request, 'main/troubleshoot/security.html')
def tshoot_common(request):
    common_issues = [
        {'issue': 'IP konflikt', 'solution': 'IP adresi üýtgediň ýa-da DHCP täzeläň'},
        {'issue': 'DNS çözmeýär', 'solution': 'DNS serwerini barlaň, hosts faýlyny barlaň'},
        {'issue': 'Baglanyşyk ýok', 'solution': 'Kabelleri, enjamlary we konfigurasiýany barlaň'},
    ]
    return render(request, 'main/troubleshoot/common.html', {'issues': common_issues})

# ==================== ÖŇDEBARYJY MÖWZULAR ====================
def advanced_index(request):
    return render(request, 'main/advanced/index.html')
def advanced_cloud(request):
    return render(request, 'main/advanced/cloud.html')
def advanced_sdn(request):
    return render(request, 'main/advanced/sdn.html')
def advanced_security(request):
    return render(request, 'main/advanced/security.html')
def advanced_ipv6(request):
    return render(request, 'main/advanced/ipv6.html')
def advanced_ipv6_addressing(request):
    return render(request, 'main/advanced/ipv6_addressing.html')
def advanced_mpls(request):
    return render(request, 'main/advanced/mpls.html')
def advanced_vpn(request):
    return render(request, 'main/advanced/vpn.html')
def advanced_qos(request):
    return render(request, 'main/advanced/qos.html')
def advanced_wireless(request):
    return render(request, 'main/advanced/wireless.html')

# ==================== KARIÝER ====================
def career_index(request):
    return render(request, 'main/career/index.html')
def career_ccna(request):
    return render(request, 'main/career/ccna.html')
def career_network_plus(request):
    return render(request, 'main/career/network_plus.html')
def career_security_plus(request):
    return render(request, 'main/career/security_plus.html')
def career_jobs(request):
    return render(request, 'main/career/jobs.html')
def career_interview(request):
    return render(request, 'main/career/interview.html')
def career_questions(request):
    questions = [
        {'question': 'OSI modelinde näçe gatlak bar?', 'answer': '7 gatlak'},
        {'question': 'TCP bilen UDP arasyndaky tapawut?', 'answer': 'TCP baglanyşyk esasly, UDP baglanyşyksyz'},
        {'question': 'Switch bilen router arasyndaky tapawut?', 'answer': 'Switch MAC adres, Router IP adres ulanyr'},
    ]
    return render(request, 'main/career/questions.html', {'questions': questions})
def career_certifications(request):
    return render(request, 'main/career/certifications.html')

# ==================== RESURSLAR ====================
def resources_index(request):
    return render(request, 'main/resources/index.html')
def resources_books(request):
    books = [
        {'title': 'CCNA 200-301 Official Cert Guide', 'author': 'Wendell Odom'},
        {'title': 'Computer Networking: A Top-Down Approach', 'author': 'Kurose & Ross'},
        {'title': 'TCP/IP Illustrated', 'author': 'Stevens'},
    ]
    return render(request, 'main/resources/books.html', {'books': books})
def resources_websites(request):
    return render(request, 'main/resources/websites.html')
def resources_forums(request):
    return render(request, 'main/resources/forums.html')
def resources_cheatsheets(request):
    return render(request, 'main/resources/cheatsheets.html')

# ==================== DIAGRAMMALAR ====================
def diagrams_index(request):
    return render(request, 'main/diagrams/index.html')
def diagram_osi(request):
    return render(request, 'main/diagrams/osi.html')
def diagram_tcpip(request):
    return render(request, 'main/diagrams/tcpip.html')
def diagram_network(request):
    return render(request, 'main/diagrams/network.html')

# ==================== ULANYJY IŞJEŇLIGI ====================
@login_required
def user_profile(request):
    return render(request, 'main/profile/index.html')
@login_required
def user_progress(request):
    # progress = UserProgress.objects.filter(user=request.user)
    return render(request, 'main/profile/progress.html')
@login_required
def user_bookmarks(request):
    return render(request, 'main/profile/bookmarks.html')
@login_required
def add_bookmark(request, lesson_id):
    # Add bookmark logic
    return redirect('user_bookmarks')
@login_required
def remove_bookmark(request, bookmark_id):
    # Remove bookmark logic
    return redirect('user_bookmarks')

# ==================== GÖZLEG ====================
def global_search(request):
    query = request.GET.get('q', '')
    results = {}
    if query:
        # Example search across models
        pass
    return render(request, 'main/search.html', {'results': results, 'query': query})

def sitemap(request):
    return render(request, 'main/sitemap.html')