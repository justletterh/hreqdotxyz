import sys,os
import curses
import aiohttp
import asyncio
import json
print('loading...')
async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://167.99.100.83:8080/status', headers={'auth': 'PASSWORD'}) as resp:
            global stats
            txt = await resp.text()
            stats = json.loads(txt)
asyncio.run(main())
psys = stats['sys']
ppc = psys['sys']
pcpu = psys['cpu']
pmem = psys['mem']
pswp = psys['mem']['swap']
pnet = psys['net']
pio = psys['io']
ppy = stats['py']
pover = stats['other-versions']
def strfix(str, tabin=1, prelen=0):
    tabnum = tabin*4
    tabnum = tabnum+prelen
    tabstr = " "*tabnum
    tabstr = "\n"+tabstr
    str = str.replace("\n", tabstr)
    return str
def draw_menu2(stdscr):
    k = 0
    cursor_x = 0
    cursor_y = 0
    stdscr.clear()
    stdscr.refresh()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_WHITE)
    while (k != ord('q')):
        if k == ord('l'):
            main()
            return
        if k == ord('p'):
            main()
            return
        stdscr.clear()
        height, width = stdscr.getmaxyx()
        if k == curses.KEY_DOWN:
            cursor_y = cursor_y + 1
        elif k == curses.KEY_UP:
            cursor_y = cursor_y - 1
        elif k == curses.KEY_RIGHT:
            cursor_x = cursor_x + 1
        elif k == curses.KEY_LEFT:
            cursor_x = cursor_x - 1
        cursor_x = max(0, cursor_x)
        cursor_x = min(width-1, cursor_x)
        cursor_y = max(0, cursor_y)
        cursor_y = min(height-1, cursor_y)
        title = "stats"[:width-1]
        subtitle = "as of rn"[:width-1]
        keystr = "Last key pressed: {}".format(k)[:width-1]
        statusbarstr = "Press 'q' to exit and 'l' or 'p' to go to the previous page | Pos: {}, {}".format(cursor_x, cursor_y)
        if k == 0:
            keystr = "No key press detected..."[:width-1]
        start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
        start_x_subtitle = int((width // 2) - (len(subtitle) // 2) - len(subtitle) % 2)
        start_x_keystr = int((width // 2) - (len(keystr) // 2) - len(keystr) % 2)
        start_y = int((height // 2) - 2)
        tab = 4
        htab = 2
        count = 0
        cond = True
        while cond:
            count = count + 1
            stdscr.addstr(count, 20, '\u2063')
            if count == height-2:
                cond = False
        stdscr.attron(curses.color_pair(2))
        stdscr.attron(curses.A_UNDERLINE)
        stdscr.attron(curses.A_BOLD)
        stdscr.addstr(1, 0, 'other versions: ')
        stdscr.attroff(curses.A_UNDERLINE)
        stdscr.addstr(2, tab*1, 'nginx: ')
        stdscr.addstr(3, tab*1, 'apt: ')
        stdscr.addstr(4, tab*1, 'nano: ')
        stdscr.attroff(curses.A_BOLD)
        stdscr.attroff(curses.color_pair(2))
        stdscr.attron(curses.color_pair(1))
        stdscr.addstr(2, 7+tab*1, strfix(f'{pover["nginx"]}', 1, 7))
        stdscr.addstr(3, 5+tab*1, strfix(f'{pover["apt"]}', 1, 5))
        stdscr.addstr(4, 6+tab*1, strfix(f'{pover["nano"]}', 1, 6))
        stdscr.attroff(curses.color_pair(1))
        name = 'STATS'
        stdscr.attron(curses.color_pair(4))
        stdscr.attron(curses.A_BOLD)
        stdscr.addstr(0, start_x_title, name)
        stdscr.addstr(0,0, ' '*start_x_title)
        stdscr.addstr(0, len(name)+start_x_title, " " * (width - len(name) - 1-start_x_title))
        stdscr.attroff(curses.A_BOLD)
        stdscr.attroff(curses.color_pair(4))
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(height-1, 0, statusbarstr)
        stdscr.addstr(height-1, len(statusbarstr), " " * (width - len(statusbarstr) - 1))
        stdscr.attroff(curses.color_pair(3))
        stdscr.move(cursor_y, cursor_x)
        stdscr.refresh()
        k = stdscr.getch()
def draw_menu(stdscr):
    k = 0
    cursor_x = 0
    cursor_y = 0
    stdscr.clear()
    stdscr.refresh()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_WHITE)
    while (k != ord('q')):
        if k == ord('n'):
            main2()
            return
        stdscr.clear()
        height, width = stdscr.getmaxyx()
        if k == curses.KEY_DOWN:
            cursor_y = cursor_y + 1
        elif k == curses.KEY_UP:
            cursor_y = cursor_y - 1
        elif k == curses.KEY_RIGHT:
            cursor_x = cursor_x + 1
        elif k == curses.KEY_LEFT:
            cursor_x = cursor_x - 1
        cursor_x = max(0, cursor_x)
        cursor_x = min(width-1, cursor_x)
        cursor_y = max(0, cursor_y)
        cursor_y = min(height-1, cursor_y)
        title = "stats"[:width-1]
        subtitle = "as of rn"[:width-1]
        keystr = "Last key pressed: {}".format(k)[:width-1]
        statusbarstr = "Press 'q' to exit and 'n' to go to the next page | Pos: {}, {}".format(cursor_x, cursor_y)
        if k == 0:
            keystr = "No key press detected..."[:width-1]
        start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
        start_x_subtitle = int((width // 2) - (len(subtitle) // 2) - len(subtitle) % 2)
        start_x_keystr = int((width // 2) - (len(keystr) // 2) - len(keystr) % 2)
        start_y = int((height // 2) - 2)
        tab = 4
        htab = 2
        count = 0
        cond = True
        while cond:
            count = count + 1
            stdscr.addstr(count, 20, '\u2063')
            if count == height-2:
                cond = False
        stdscr.attron(curses.color_pair(2))
        stdscr.attron(curses.A_UNDERLINE)
        stdscr.attron(curses.A_BOLD)
        stdscr.addstr(1, 0, 'system:')
        stdscr.addstr(2, tab*1, 'computer:')
        stdscr.addstr(9, tab*1, 'cpu:')
        stdscr.addstr(14, tab*1, 'memory:')
        stdscr.addstr(19, tab*2, 'swap:')
        stdscr.addstr(24, tab*1, 'network:')
        stdscr.addstr(29, tab*1, 'input/output:')
        stdscr.addstr(32, 0, 'python:')
        stdscr.attroff(curses.A_UNDERLINE)
        stdscr.addstr(3, tab*2, 'os: ')
        stdscr.addstr(4, tab*2, 'name: ')
        stdscr.addstr(5, tab*2, 'os release: ')
        stdscr.addstr(6, tab*2, 'os version: ')
        stdscr.addstr(7, tab*2, 'architecture: ')
        stdscr.addstr(8, tab*2, 'boot time: ')
        stdscr.addstr(10, tab*2, 'current frequency: ')
        stdscr.addstr(11, tab*2, 'physical cores: ')
        stdscr.addstr(12, tab*2, 'total cores: ')
        stdscr.addstr(13, tab*2, 'usage: ')
        stdscr.addstr(15, tab*2, 'total: ')
        stdscr.addstr(16, tab*2, 'avaliable: ')
        stdscr.addstr(17, tab*2, 'used: ')
        stdscr.addstr(18, tab*2, 'percent free: ')
        stdscr.addstr(20, tab*3, 'total: ')
        stdscr.addstr(21, tab*3, 'free: ')
        stdscr.addstr(22, tab*3, 'used: ')
        stdscr.addstr(23, tab*3, 'percent used: ')
        stdscr.addstr(25, tab*2, 'interface name: ')
        stdscr.addstr(26, tab*2, 'ip: ')
        stdscr.addstr(27, tab*2, 'netmask: ')
        stdscr.addstr(28, tab*2, 'broadcast ip: ')
        stdscr.addstr(30, tab*2, 'sent: ')
        stdscr.addstr(31, tab*2, 'received: ')
        stdscr.addstr(33, tab*1, 'version: ')
        stdscr.addstr(35, tab*1, 'version info: ')
        stdscr.attroff(curses.A_BOLD)
        stdscr.attroff(curses.color_pair(2))
        stdscr.attron(curses.color_pair(1))
        stdscr.addstr(3, 4+tab*2, f'{ppc["os"]}')
        stdscr.addstr(4, 6+tab*2, f'{ppc["node"]}')
        stdscr.addstr(5, 12+tab*2, f'{ppc["release"]}')
        stdscr.addstr(6, 12+tab*2, f'{ppc["ver"]}')
        stdscr.addstr(7, 14+tab*2, f'{ppc["arch"]}')
        stdscr.addstr(8, 11+tab*2, f'{ppc["start"]}')
        stdscr.addstr(10, 19+tab*2, f'{pcpu["curfreq"]}')
        stdscr.addstr(11, 16+tab*2, f'{pcpu["phys"]}')
        stdscr.addstr(12, 13+tab*2, f'{pcpu["total"]}')
        stdscr.addstr(13, 7+tab*2, f'{pcpu["use"]}')
        stdscr.addstr(15, 7+tab*2, f'{pmem["total"]}')
        stdscr.addstr(16, 11+tab*2, f'{pmem["avaliable"]}')
        stdscr.addstr(17, 6+tab*2, f'{pmem["used"]}')
        stdscr.addstr(18, 14+tab*2, f'{pmem["percnt"]}')
        stdscr.addstr(20, 7+tab*3, f'{pswp["total"]}')
        stdscr.addstr(21, 6+tab*3, f'{pswp["free"]}')
        stdscr.addstr(22, 6+tab*3, f'{pswp["used"]}')
        stdscr.addstr(23, 14+tab*3, f'{pswp["percnt"]}')
        stdscr.addstr(25, 16+tab*2, f'{pnet["name"]}')
        stdscr.addstr(26, 4+tab*2, f'{pnet["ip"]}')
        stdscr.addstr(27, 9+tab*2, f'{pnet["mask"]}')
        stdscr.addstr(28, 14+tab*2, f'{pnet["bip"]}')
        stdscr.addstr(30, 6+tab*2, f'{pio["sent"]}')
        stdscr.addstr(31, 10+tab*2, f'{pio["rcved"]}')
        stdscr.addstr(33, 9+tab*1, strfix(f'{ppy["ver"]}', 1, 9))
        stdscr.addstr(35, 14+tab*1, f'{ppy["verinf"]}')
        stdscr.attroff(curses.color_pair(1))
        name = 'STATS'
        stdscr.attron(curses.color_pair(4))
        stdscr.attron(curses.A_BOLD)
        stdscr.addstr(0, start_x_title, name)
        stdscr.addstr(0,0, ' '*start_x_title)
        stdscr.addstr(0, len(name)+start_x_title, " " * (width - len(name) - 1-start_x_title))
        stdscr.attroff(curses.A_BOLD)
        stdscr.attroff(curses.color_pair(4))
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(height-1, 0, statusbarstr)
        stdscr.addstr(height-1, len(statusbarstr), " " * (width - len(statusbarstr) - 1))
        stdscr.attroff(curses.color_pair(3))
        stdscr.move(cursor_y, cursor_x)
        stdscr.refresh()
        k = stdscr.getch()
def main():
    curses.wrapper(draw_menu)
def main2():
    curses.wrapper(draw_menu2)
if __name__ == "__main__":
    main()