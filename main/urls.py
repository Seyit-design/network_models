from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # Esasy sahypa
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Kategoriýalar
    path('categories/', views.category_list, name='category_list'),
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    
    # OSI Model
    path('osi/', views.osi_index, name='osi_index'),
    path('osi/layer/<int:layer>/', views.osi_layer_detail, name='osi_layer_detail'),
    path('osi/layer1/', views.osi_layer1, name='osi_layer1'),
    path('osi/layer2/', views.osi_layer2, name='osi_layer2'),
    path('osi/layer3/', views.osi_layer3, name='osi_layer3'),
    path('osi/layer4/', views.osi_layer4, name='osi_layer4'),
    path('osi/layer5/', views.osi_layer5, name='osi_layer5'),
    path('osi/layer6/', views.osi_layer6, name='osi_layer6'),
    path('osi/layer7/', views.osi_layer7, name='osi_layer7'),
    
    # TCP/IP Model
    path('tcpip/', views.tcpip_index, name='tcpip_index'),
    path('tcpip/layer/<int:layer>/', views.tcpip_layer_detail, name='tcpip_layer_detail'),
    path('tcpip/layer1/', views.tcpip_layer1, name='tcpip_layer1'),
    path('tcpip/layer2/', views.tcpip_layer2, name='tcpip_layer2'),
    path('tcpip/layer3/', views.tcpip_layer3, name='tcpip_layer3'),
    path('tcpip/layer4/', views.tcpip_layer4, name='tcpip_layer4'),
    path('tcpip/layer5/', views.tcpip_layer5, name='tcpip_layer5'),
    
    # Esasy tor düşünjeleri
    path('basic/', views.basic_index, name='basic_index'),
    path('basic/ip-address/', views.basic_ip, name='basic_ip'),
    path('basic/ip-address/classes/', views.basic_ip_classes, name='basic_ip_classes'),
    path('basic/mac-address/', views.basic_mac, name='basic_mac'),
    path('basic/subnetting/', views.basic_subnetting, name='basic_subnetting'),
    path('basic/vlan/', views.basic_vlan, name='basic_vlan'),
    path('basic/nat/', views.basic_nat, name='basic_nat'),
    path('basic/public-private-ip/', views.basic_public_private, name='basic_public_private'),
    
    # Tor enjamlary
    path('devices/', views.devices_index, name='devices_index'),
    path('devices/router/', views.device_router, name='device_router'),
    path('devices/switch/', views.device_switch, name='device_switch'),
    path('devices/hub/', views.device_hub, name='device_hub'),
    path('devices/firewall/', views.device_firewall, name='device_firewall'),
    path('devices/access-point/', views.device_ap, name='device_ap'),
    path('devices/modem/', views.device_modem, name='device_modem'),
    path('devices/repeater/', views.device_repeater, name='device_repeater'),
    path('devices/bridge/', views.device_bridge, name='device_bridge'),
    path('devices/gateway/', views.device_gateway, name='device_gateway'),
    path('devices/comparison/', views.device_comparison, name='device_comparison'),
    
    # Protokollar
    path('protocols/', views.protocols_index, name='protocols_index'),
    path('protocols/tcp/', views.protocol_tcp, name='protocol_tcp'),
    path('protocols/udp/', views.protocol_udp, name='protocol_udp'),
    path('protocols/ip/', views.protocol_ip, name='protocol_ip'),
    path('protocols/icmp/', views.protocol_icmp, name='protocol_icmp'),
    path('protocols/arp/', views.protocol_arp, name='protocol_arp'),
    path('protocols/dhcp/', views.protocol_dhcp, name='protocol_dhcp'),
    path('protocols/dns/', views.protocol_dns, name='protocol_dns'),
    path('protocols/http/', views.protocol_http, name='protocol_http'),
    path('protocols/https/', views.protocol_https, name='protocol_https'),
    path('protocols/ftp/', views.protocol_ftp, name='protocol_ftp'),
    path('protocols/smtp/', views.protocol_smtp, name='protocol_smtp'),
    path('protocols/pop3/', views.protocol_pop3, name='protocol_pop3'),
    path('protocols/imap/', views.protocol_imap, name='protocol_imap'),
    path('protocols/ssh/', views.protocol_ssh, name='protocol_ssh'),
    path('protocols/telnet/', views.protocol_telnet, name='protocol_telnet'),
    path('protocols/snmp/', views.protocol_snmp, name='protocol_snmp'),
    path('protocols/comparison/', views.protocol_comparison, name='protocol_comparison'),
    path('protocols/port-numbers/', views.protocol_ports, name='protocol_ports'),
    
    # Kabeller we birikmeler
    path('cables/', views.cables_index, name='cables_index'),
    path('cables/ethernet/', views.cable_ethernet, name='cable_ethernet'),
    path('cables/ethernet/cat5/', views.cable_cat5, name='cable_cat5'),
    path('cables/ethernet/cat5e/', views.cable_cat5e, name='cable_cat5e'),
    path('cables/ethernet/cat6/', views.cable_cat6, name='cable_cat6'),
    path('cables/ethernet/cat7/', views.cable_cat7, name='cable_cat7'),
    path('cables/fiber/', views.cable_fiber, name='cable_fiber'),
    path('cables/fiber/single-mode/', views.fiber_single_mode, name='fiber_single_mode'),
    path('cables/fiber/multi-mode/', views.fiber_multi_mode, name='fiber_multi_mode'),
    path('cables/coaxial/', views.cable_coaxial, name='cable_coaxial'),
    path('cables/serial/', views.cable_serial, name='cable_serial'),
    path('cables/console/', views.cable_console, name='cable_console'),
    path('cables/usb/', views.cable_usb, name='cable_usb'),
    path('cables/wireless/', views.wireless_index, name='wireless_index'),
    path('cables/wireless/wi-fi/', views.wireless_wifi, name='wireless_wifi'),
    path('cables/wireless/bluetooth/', views.wireless_bluetooth, name='wireless_bluetooth'),
    path('cables/wireless/cellular/', views.wireless_cellular, name='wireless_cellular'),
    path('cables/crimping/', views.cable_crimping, name='cable_crimping'),
    path('cables/color-codes/', views.cable_colors, name='cable_colors'),
    
    # Topologiýalar
    path('topologies/', views.topologies_index, name='topologies_index'),
    path('topologies/star/', views.topology_star, name='topology_star'),
    path('topologies/bus/', views.topology_bus, name='topology_bus'),
    path('topologies/ring/', views.topology_ring, name='topology_ring'),
    path('topologies/mesh/', views.topology_mesh, name='topology_mesh'),
    path('topologies/tree/', views.topology_tree, name='topology_tree'),
    path('topologies/hybrid/', views.topology_hybrid, name='topology_hybrid'),
    path('topologies/daisy-chain/', views.topology_daisy, name='topology_daisy'),
    path('topologies/comparison/', views.topology_comparison, name='topology_comparison'),
    
    # IP adresleme we kalkulýatorlar
    path('tools/', views.tools_index, name='tools_index'),
    path('tools/ip-calculator/', views.ip_calculator, name='ip_calculator'),
    path('tools/ip-calculator/result/', views.ip_calculator_result, name='ip_calculator_result'),
    path('tools/subnet-calculator/', views.subnet_calculator, name='subnet_calculator'),
    path('tools/subnet-calculator/result/', views.subnet_calculator_result, name='subnet_calculator_result'),
    path('tools/vlsm-calculator/', views.vlsm_calculator, name='vlsm_calculator'),
    path('tools/mac-converter/', views.mac_converter, name='mac_converter'),
    path('tools/binary-converter/', views.binary_converter, name='binary_converter'),
    path('tools/hex-converter/', views.hex_converter, name='hex_converter'),
    path('tools/port-scanner/', views.port_scanner, name='port_scanner'),
    path('tools/ping-test/', views.ping_test, name='ping_test'),
    path('tools/traceroute/', views.traceroute, name='traceroute'),
    path('tools/mac-finder/', views.mac_finder, name='mac_finder'),
    path('tools/wildcard-calculator/', views.wildcard_calculator, name='wildcard_calculator'),
    
    # Amaly maşklar
    path('exercises/', views.exercises_index, name='exercises_index'),
    path('exercises/subnetting/', views.ex_subnetting, name='ex_subnetting'),
    path('exercises/subnetting/basic/', views.ex_subnetting_basic, name='ex_subnetting_basic'),
    path('exercises/subnetting/intermediate/', views.ex_subnetting_intermediate, name='ex_subnetting_intermediate'),
    path('exercises/subnetting/advanced/', views.ex_subnetting_advanced, name='ex_subnetting_advanced'),
    path('exercises/ip-classes/', views.ex_ip_classes, name='ex_ip_classes'),
    path('exercises/vlsm/', views.ex_vlsm, name='ex_vlsm'),
    path('exercises/cabling/', views.ex_cabling, name='ex_cabling'),
    path('exercises/routing/', views.ex_routing, name='ex_routing'),
    path('exercises/subnetting/check/', views.ex_subnetting_check, name='ex_subnetting_check'),
    
    # Interaktiw oýunlar
    path('games/', views.games_index, name='games_index'),
    path('games/layer-quiz/', views.game_layer_quiz, name='game_layer_quiz'),
    path('games/layer-quiz/check/', views.game_layer_quiz_check, name='game_layer_quiz_check'),
    path('games/protocol-match/', views.game_protocol_match, name='game_protocol_match'),
    path('games/drag-drop/', views.game_drag_drop, name='game_drag_drop'),
    path('games/ip-game/', views.game_ip_game, name='game_ip_game'),
    path('games/memory-game/', views.game_memory, name='game_memory'),
    
    # Wideo dersler
    path('videos/', views.videos_index, name='videos_index'),
    path('videos/osi-model/', views.video_osi, name='video_osi'),
    path('videos/tcpip/', views.video_tcpip, name='video_tcpip'),
    path('videos/routing/', views.video_routing, name='video_routing'),
    path('videos/switching/', views.video_switching, name='video_switching'),
    path('videos/subnetting/', views.video_subnetting, name='video_subnetting'),
    path('videos/<int:video_id>/', views.video_detail, name='video_detail'),
    
    # Testler
    path('quiz/', views.quiz_index, name='quiz_index'),
    path('quiz/osi/', views.quiz_osi, name='quiz_osi'),
    path('quiz/tcpip/', views.quiz_tcpip, name='quiz_tcpip'),
    path('quiz/protocols/', views.quiz_protocols, name='quiz_protocols'),
    path('quiz/devices/', views.quiz_devices, name='quiz_devices'),
    path('quiz/ip-addressing/', views.quiz_ip, name='quiz_ip'),
    path('quiz/<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
    path('quiz/<int:quiz_id>/submit/', views.quiz_submit, name='quiz_submit'),
    path('quiz/result/<int:result_id>/', views.quiz_result, name='quiz_result'),
    path('quiz/leaderboard/', views.quiz_leaderboard, name='quiz_leaderboard'),
    
    # Sözlük
    path('glossary/', views.glossary_index, name='glossary_index'),
    path('glossary/search/', views.glossary_search, name='glossary_search'),
    path('glossary/<str:term>/', views.glossary_detail, name='glossary_detail'),
    path('glossary/letter/<str:letter>/', views.glossary_by_letter, name='glossary_by_letter'),
    
    # Laboratoriýalar
    path('labs/', views.labs_index, name='labs_index'),
    path('labs/packet-tracer/', views.lab_packet_tracer, name='lab_packet_tracer'),
    path('labs/cisco-commands/', views.lab_cisco_commands, name='lab_cisco_commands'),
    path('labs/network-simulation/', views.lab_simulation, name='lab_simulation'),
    path('labs/basic-config/', views.lab_basic_config, name='lab_basic_config'),
    path('labs/vlan-config/', views.lab_vlan_config, name='lab_vlan_config'),
    path('labs/routing-config/', views.lab_routing_config, name='lab_routing_config'),
    
    # Troubleshooting
    path('troubleshoot/', views.troubleshoot_index, name='troubleshoot_index'),
    path('troubleshoot/connectivity/', views.tshoot_connectivity, name='tshoot_connectivity'),
    path('troubleshoot/dns/', views.tshoot_dns, name='tshoot_dns'),
    path('troubleshoot/ip-conflict/', views.tshoot_ip_conflict, name='tshoot_ip_conflict'),
    path('troubleshoot/performance/', views.tshoot_performance, name='tshoot_performance'),
    path('troubleshoot/security/', views.tshoot_security, name='tshoot_security'),
    path('troubleshoot/common-issues/', views.tshoot_common, name='tshoot_common'),
    
    # Öňdebaryjy mövzular
    path('advanced/', views.advanced_index, name='advanced_index'),
    path('advanced/cloud-networking/', views.advanced_cloud, name='advanced_cloud'),
    path('advanced/sdn/', views.advanced_sdn, name='advanced_sdn'),
    path('advanced/network-security/', views.advanced_security, name='advanced_security'),
    path('advanced/ipv6/', views.advanced_ipv6, name='advanced_ipv6'),
    path('advanced/ipv6/addressing/', views.advanced_ipv6_addressing, name='advanced_ipv6_addressing'),
    path('advanced/mpls/', views.advanced_mpls, name='advanced_mpls'),
    path('advanced/vpn/', views.advanced_vpn, name='advanced_vpn'),
    path('advanced/qos/', views.advanced_qos, name='advanced_qos'),
    path('advanced/wireless/', views.advanced_wireless, name='advanced_wireless'),
    
    # Kariýer
    path('career/', views.career_index, name='career_index'),
    path('career/ccna/', views.career_ccna, name='career_ccna'),
    path('career/network-plus/', views.career_network_plus, name='career_network_plus'),
    path('career/security-plus/', views.career_security_plus, name='career_security_plus'),
    path('career/jobs/', views.career_jobs, name='career_jobs'),
    path('career/interview/', views.career_interview, name='career_interview'),
    path('career/interview/questions/', views.career_questions, name='career_questions'),
    path('career/certifications/', views.career_certifications, name='career_certifications'),
    
    # Resurslar
    path('resources/', views.resources_index, name='resources_index'),
    path('resources/books/', views.resources_books, name='resources_books'),
    path('resources/websites/', views.resources_websites, name='resources_websites'),
    path('resources/forums/', views.resources_forums, name='resources_forums'),
    path('resources/cheatsheets/', views.resources_cheatsheets, name='resources_cheatsheets'),
    
    # Diagrammalar
    path('diagrams/', views.diagrams_index, name='diagrams_index'),
    path('diagrams/osi/', views.diagram_osi, name='diagram_osi'),
    path('diagrams/tcpip/', views.diagram_tcpip, name='diagram_tcpip'),
    path('diagrams/network/', views.diagram_network, name='diagram_network'),
    
    # Ulanyjy işjeňligi
    path('profile/', views.user_profile, name='user_profile'),
    path('progress/', views.user_progress, name='user_progress'),
    path('bookmarks/', views.user_bookmarks, name='user_bookmarks'),
    path('bookmark/add/<int:lesson_id>/', views.add_bookmark, name='add_bookmark'),
    path('bookmark/remove/<int:bookmark_id>/', views.remove_bookmark, name='remove_bookmark'),
    
    # Gözleg
    path('search/', views.global_search, name='global_search'),
    path('sitemap/', views.sitemap, name='sitemap'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)