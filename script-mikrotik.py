from netmiko import ConnectHandler

router_mikrotik = {
    'device_type': 'mikrotik_routeros',
    'host':   '10.0.0.140',
    'username': 'admin',
    'password': 'admin',
    'port': 22,            # optional, defaults to 22
    'secret': '',          # optional, defaults to ''
}

conexion = ConnectHandler(**router_mikrotik)

# Definir comandos a ejecutar
configurar = [
        '/interface wireless security-profiles set [ find default=yes ] supplicant-identity=MikroTik',
        '/ip pool add name=dhcp_pool2 ranges=172.25.18.129-172.25.18.254',
        '/ip dhcp-server add address-pool=dhcp_pool2 interface=ether3 name=dhcp1',
        '/port set 0 name=serial0 set 1 name=serial1',
        '/ip address add address=10.0.3.1/24 interface=ether3 network=10.0.3.0 add address=172.25.18.1/25 interface=ether2 network=172.25.18.0',
        '/ip dhcp-client add interface=ether1 add interface=ether2',
        '/ip dhcp-server network add address=172.25.18.128/25 gateway=172.25.18.129',
        '/ip dns set allow-remote-requests=yes servers=8.8.8.8',
        '/ip firewall nat add action=masquerade chain=srcnat out-interface=ether1',
]

# Ejecutar comandos (send_config_set - para enviar comandos de configuración)
accion1 = conexion.send_config_set(configurar)
print(accion1)

# Cerrar la conexión
conexion.disconnect()