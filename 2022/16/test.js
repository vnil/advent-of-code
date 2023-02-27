const k = `Valve UU has flow rate=24; tunnels lead to valves MO, FW, LQ
Valve EW has flow rate=16; tunnels lead to valves YZ, JK, SG
Valve RQ has flow rate=0; tunnels lead to valves ER, ZI
Valve WJ has flow rate=25; tunnel leads to valve XP
Valve OZ has flow rate=17; tunnels lead to valves UB, HK, JM, ZK, ER
Valve ZM has flow rate=23; tunnel leads to valve GB
Valve BE has flow rate=0; tunnels lead to valves AA, MJ
Valve YZ has flow rate=0; tunnels lead to valves KC, EW
Valve JX has flow rate=0; tunnels lead to valves WH, KI
Valve QC has flow rate=0; tunnels lead to valves MJ, DW
Valve RU has flow rate=14; tunnel leads to valve SU
Valve NI has flow rate=0; tunnels lead to valves AA, WH
Valve XP has flow rate=0; tunnels lead to valves WJ, TM
Valve FW has flow rate=0; tunnels lead to valves UU, VO
Valve TM has flow rate=0; tunnels lead to valves PL, XP
Valve KJ has flow rate=0; tunnels lead to valves MJ, CO
Valve LQ has flow rate=0; tunnels lead to valves UU, PE
Valve PE has flow rate=0; tunnels lead to valves YJ, LQ
Valve WH has flow rate=11; tunnels lead to valves HK, JX, EZ, ZU, NI
Valve ZB has flow rate=0; tunnels lead to valves AA, AC
Valve GA has flow rate=0; tunnels lead to valves AA, CO
Valve NH has flow rate=0; tunnels lead to valves ZU, MJ
Valve SG has flow rate=0; tunnels lead to valves PY, EW
Valve MJ has flow rate=6; tunnels lead to valves KJ, BE, QC, NH, EE
Valve QX has flow rate=0; tunnels lead to valves UD, PL
Valve ZK has flow rate=0; tunnels lead to valves FD, OZ
Valve GB has flow rate=0; tunnels lead to valves ZM, FD
Valve ZU has flow rate=0; tunnels lead to valves NH, WH
Valve MO has flow rate=0; tunnels lead to valves ZI, UU
Valve KI has flow rate=0; tunnels lead to valves DW, JX
Valve UD has flow rate=19; tunnels lead to valves VO, PY, QX
Valve VO has flow rate=0; tunnels lead to valves UD, FW
Valve PM has flow rate=0; tunnels lead to valves YF, FD
Valve FD has flow rate=21; tunnels lead to valves ZK, PM, GB
Valve NQ has flow rate=0; tunnels lead to valves SU, DW
Valve YF has flow rate=0; tunnels lead to valves ZI, PM
Valve CO has flow rate=18; tunnels lead to valves GA, KJ, EZ
Valve DW has flow rate=10; tunnels lead to valves NQ, QC, KI, JK, HX
Valve PL has flow rate=22; tunnels lead to valves KC, TM, QX
Valve AC has flow rate=0; tunnels lead to valves ZB, YJ
Valve YJ has flow rate=15; tunnels lead to valves OC, PE, AC
Valve SU has flow rate=0; tunnels lead to valves NQ, RU
Valve ZI has flow rate=20; tunnels lead to valves YF, RQ, MO
Valve EZ has flow rate=0; tunnels lead to valves WH, CO
Valve HX has flow rate=0; tunnels lead to valves AA, DW
Valve EE has flow rate=0; tunnels lead to valves JM, MJ
Valve KC has flow rate=0; tunnels lead to valves YZ, PL
Valve AA has flow rate=0; tunnels lead to valves ZB, BE, NI, HX, GA
Valve UB has flow rate=0; tunnels lead to valves OC, OZ
Valve HK has flow rate=0; tunnels lead to valves OZ, WH
Valve PY has flow rate=0; tunnels lead to valves UD, SG
Valve JK has flow rate=0; tunnels lead to valves EW, DW
Valve OC has flow rate=0; tunnels lead to valves YJ, UB
Valve ER has flow rate=0; tunnels lead to valves RQ, OZ
Valve JM has flow rate=0; tunnels lead to valves OZ, EE`.split('\n')

k.sort((a, b) => a.substring(0, 10).localeCompare(b.substring(0, 10)))
console.log(k)


exit()
visited = set()
openable_pipes = len([a for a in pipes if rates[a] > 0])
mem = defaultdict(lambda: 999999)
M = int(sys.argv[2]) 
opened = set()

max_pressure = sum(rates.values())
q = deque([('AA', 'AA', 0, set(), 0, 0)])

max_p = 0
# open as many as possible as fast as possible
some = defaultdict(lambda: (9999, 0))
print(max_pressure)
best = defaultdict(lambda: 0)
i = 0
#2983

while q:
    me, elephant, minute, opened, pressure, acc = q.pop()

    if minute > 14 and best[minute] > pressure:
        continue
    if minute > 8 and pressure == 0:
        continue
    if minute > 12 and pressure < 60:
        continue
    best[minute] = pressure
    if minute == M:
        if acc > max_p:
            max_p = acc # +1 eller inte?
            print(acc)

        continue
    i+=1
    if i%1000000==0:
        print(i, len(q))

    opened_key = ''.join(sorted(opened))
    mem_key = (me, elephant, minute, acc, opened_key)
    if mem[mem_key] <= minute:
        continue
    mem[mem_key] = minute
    if some[(me, elephant)][0] < minute and some[(me, elephant)][1] >= pressure:
        continue 
    some[(me, elephant)] = (minute, pressure)


    if pressure == max_pressure:
        n = acc+pressure*(M-minute)
        if n > max_p:
            max_p = n
            print(n)
        
        continue
    for me_target in g[me]:
        for elephant_target in g[elephant]:
            q.append((me_target, elephant_target, minute + 1, opened, pressure, acc+pressure))
            new_opened = set(opened)
            a, b = False, False
            if me not in new_opened and rates[me] > 0:
                new_opened.add(me)
                q.append((me, elephant_target, minute + 1, new_opened, pressure+rates[me], acc+pressure))
                a = True
            if elephant not in new_opened and rates[elephant] > 0:
                new_opened.add(elephant)
                q.append((me_target, elephant, minute + 1, new_opened, pressure+rates[elephant], acc+pressure))
                b = True
            if a and b:
                q.append((me, elephant, minute + 1, new_opened, pressure+rates[elephant]+rates[me], acc+pressure))
print(max_p)

