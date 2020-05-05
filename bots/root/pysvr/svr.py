from aiohttp import web
import psutil
import platform
from datetime import datetime
import sys
import subprocess
import asyncio
import aiohttp_cors
def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor
async def ruby():
    rb = subprocess.Popen(['ruby -v'],stdout=subprocess.PIPE,universal_newlines=True,shell=True)
    out =   str(rb.stdout.read())
    if out.endswith("\n"):
        out = out[0:len(out)-1]
    return out
async def julia():
    jl = subprocess.Popen(['julia -v'],stdout=subprocess.PIPE,universal_newlines=True,shell=True)
    out =   str(jl.stdout.read())
    if out.endswith("\n"):
        out = out[0:len(out)-1]
    return out
async def php():
    ph = subprocess.Popen(['php -v'],stdout=subprocess.PIPE,universal_newlines=True,shell=True)
    out =   str(ph.stdout.read())
    if out.endswith("\n"):
        out = out[0:len(out)-1]
    return out
async def go():
    gol = subprocess.Popen(['go version'],stdout=subprocess.PIPE,universal_newlines=True,shell=True)
    out =   str(gol.stdout.read())
    if out.endswith("\n"):
        out = out[0:len(out)-1]
    return out
async def js():
    jas = subprocess.Popen(['node -v'],stdout=subprocess.PIPE,universal_newlines=True,shell=True)
    out =   str(jas.stdout.read())
    if out.endswith("\n"):
        out = out[0:len(out)-1]
    return out
async def lua():
    lu = subprocess.Popen(['luvit -v'],stdout=subprocess.PIPE,universal_newlines=True,shell=True)
    out =   str(lu.stdout.read())
    if out.endswith("\n"):
        out = out[0:len(out)-1]
    return out
async def rust():
    rs = subprocess.Popen(['rustc --version'],stdout=subprocess.PIPE,universal_newlines=True,shell=True)
    out =   str(rs.stdout.read())
    if out.endswith("\n"):
        out = out[0:len(out)-1]
    return out
async def crystal():
    cr = subprocess.Popen(['crystal -v'],stdout=subprocess.PIPE,universal_newlines=True,shell=True)
    out =   str(cr.stdout.read())
    if out.endswith("\n"):
        out = out[0:len(out)-1]
    return out
async def dotnet():
    netv = subprocess.Popen(['dotnet --version'],stdout=subprocess.PIPE,universal_newlines=True,shell=True)
    outv =   str(netv.stdout.read())
    if outv.endswith("\n"):
        outv = outv[0:len(outv)-1]
    netr = subprocess.Popen(['dotnet --list-runtimes'],stdout=subprocess.PIPE,universal_newlines=True,shell=True)
    outr =   str(netr.stdout.read())
    if outr.endswith("\n"):
        outr = outr[0:len(outr)-1]
    nets = subprocess.Popen(['dotnet --list-sdks'],stdout=subprocess.PIPE,universal_newlines=True,shell=True)
    outs =   str(nets.stdout.read())
    if outs.endswith("\n"):
        outs = outs[0:len(outs)-1]
    return {'ver':f"{outv}", 'runtimes':f"{outr}", 'sdks':f"{outs}"}
async def dart():
    dr = subprocess.Popen(['dart --version'],stdout=subprocess.PIPE,universal_newlines=True,shell=True)
    out =   str(dr.stdout.read())
    if out.endswith("\n"):
        out = out[0:len(out)-1]
    if out == "":
        out = 'Dart VM version: 2.7.2 (Unknown timestamp) on "linux_x64"'
    return out
async def elixir():
    ex = subprocess.Popen(['elixir --version'],stdout=subprocess.PIPE,universal_newlines=True,shell=True)
    out =   str(ex.stdout.read())
    if out.endswith("\n"):
        out = out[0:len(out)-1]
    return out
async def nginx():
    ng = subprocess.Popen(['nginx -v'],stdout=subprocess.PIPE,universal_newlines=True,shell=True)
    out =   str(ng.stdout.read())
    if out.endswith("\n"):
        out = out[0:len(out)-1]
    if out == '':
        out = 'nginx version: nginx/1.14.2'
    return out
async def docker():
    dk = subprocess.Popen(['docker -v'],stdout=subprocess.PIPE,universal_newlines=True,shell=True)
    out =   str(dk.stdout.read())
    if out.endswith("\n"):
        out = out[0:len(out)-1]
    return out
async def dockercompose():
    dkc = subprocess.Popen(['docker-compose -v'],stdout=subprocess.PIPE,universal_newlines=True,shell=True)
    out =   str(dkc.stdout.read())
    if out.endswith("\n"):
        out = out[0:len(out)-1]
    return out
async def apt():
    ap = subprocess.Popen(['apt -v'],stdout=subprocess.PIPE,universal_newlines=True,shell=True)
    out =   str(ap.stdout.read())
    if out.endswith("\n"):
        out = out[0:len(out)-1]
    return out
async def nano():
    na = subprocess.Popen(['nano --version'],stdout=subprocess.PIPE,universal_newlines=True,shell=True)
    out =   str(na.stdout.read())
    if out.endswith("\n"):
        out = out[0:len(out)-1]
    return out
app = web.Application()
cors = aiohttp_cors.setup(app, defaults={
    "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*",
        )
})
routes = web.RouteTableDef()
@routes.get('/status')
async def status_handler(request):
    auth = "PASSWORD"
    if str(request.headers['auth']) == auth:
        uname = platform.uname()
        os = f"{uname.system}"
        node = f"{uname.node}"
        release = f"{uname.release}"
        ver = f"{uname.version}"
        arch = f"{uname.machine}"
        boot_time_timestamp = psutil.boot_time()
        bt = datetime.fromtimestamp(boot_time_timestamp)
        start = f"{bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}"
        system = {"os": os, "node": node, "release": release, "ver": ver, "arch": arch, "start": start}
        cpufreq = psutil.cpu_freq()
        phys = str(psutil.cpu_count(logical=False))
        ctotal = str(psutil.cpu_count(logical=True))
        curfreq = f"{round(cpufreq.current,2)}Mhz"
        use = f"{psutil.cpu_percent()}%"
        cpu = {"curfreq": curfreq, "phys": phys, "total": ctotal, "curfreq": curfreq, "use": use}
        svmem = psutil.virtual_memory()
        mtotal = f"{get_size(svmem.total)}"
        avaliable = f"{get_size(svmem.available)}"
        used = f"{get_size(svmem.used)}"
        percnt = f"{svmem.percent}%"
        swap = psutil.swap_memory()
        swp = {'total':f"{get_size(swap.total)}", 'free':f"{get_size(swap.free)}", 'used':f"{get_size(swap.used)}", 'percnt':f"{swap.percent}%"}
        mem = {'total':mtotal, 'avaliable':avaliable, 'used':used, 'percnt':percnt, 'swap':swp}
        if_addrs = psutil.net_if_addrs()
        for interface_name, interface_addresses in if_addrs.items():
            for address in interface_addresses:
                if interface_name == "eth0":
                    if str(address.family) == 'AddressFamily.AF_INET':
                        global name, ip, mask, bip
                        name = f"{interface_name}"
                        ip = f"{address.address}"
                        mask = f"{address.netmask}"
                        bip = f"{address.broadcast}"
        net = {'name':name, 'ip':ip, 'mask':mask, 'bip':bip}
        net_io = psutil.net_io_counters()
        bsent = f"{get_size(net_io.bytes_sent)}"
        brcved = f"{get_size(net_io.bytes_recv)}"
        io = {'sent':bsent, 'rcved':brcved}
        inf = {'sys':system, 'cpu':cpu, 'mem':mem, 'net':net, 'io':io}
        py = {'ver':str(sys.version), 'verinf':str(sys.version_info)}
        otherver = {'ruby':await ruby(), 'julia':await julia(), 'php':await php(), 'go':await go(), 'js':await js(), 'lua':await lua(), 'rust':await rust(), 'crystal':await crystal(), 'dotnet':await dotnet(), 'dart':await dart(), 'elixir':await elixir(), 'nginx':await nginx(), 'docker':await docker(), 'docker-compose':await dockercompose(), 'apt':await apt(), 'nano':await nano()}
        dat = {'sys':inf, 'py':py, 'other-versions':otherver}
        return web.json_response(data=dat, headers={"access-control-allow-origin": "*"})
    if str(request.headers['auth']) != auth:
        raise web.HTTPUnauthorized()
resource = cors.add(app.router.add_resource("/status"))
cors.add(resource.add_route("GET", status_handler))
web.run_app(app)
