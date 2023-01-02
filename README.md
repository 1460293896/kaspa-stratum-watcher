# kaspa stratum watcher
We can analyze packets and develop the tools we need

## Use miner connects to a pool
```bash=

# https://github.com/doktor83/SRBMiner-Multi/releases
# https://kaspa.acc-pool.pw/miners/qzda5cyaxsj0qg889p94xdmm93aj3awcqhz8ht9c54l9gs7u34f02gspz74n3/
consoles1:~/>python stratum_watcher.py

consoles2:~/>./SRBMiner-MULTI --algorithm kaspa --pool localhost:5555 --wallet kaspa:qzda5cyaxsj0qg889p94xdmm93aj3awcqhz8ht9c54l9gs7u34f02gspz74n3 --password x --worker PikaC
```
Result :
```bash=
............ kaspa stratum bridge (submit and result is true)
==> b'{"id": 2876640, "method": "mining.notify", "params": ["51", [346519526552184601, 12432088765924027308, 134308965009666439
25, 4990493586688826218], 1666417033635]}\n'
<== b'{"method":"mining.submit","id":11,"params":["kaspa:qrygml00m4v9wp4stz4875jxak457up20a78yuw8p20ytd9m349773unp87ps","51","0
xf88058944003f3d0"],"error":null}\n'
==> b'{"id": 11, "result": true, "error": null}\n'

==> b'{"id": 2876654, "method": "mining.notify", "params": ["5f", [3402437907395415126, 16019740718156547242, 10510275512913815
450, 7662923120300235366], 1666417052179]}\n'
<== b'{"method":"mining.submit","id":12,"params":["kaspa:qrygml00m4v9wp4stz4875jxak457up20a78yuw8p20ytd9m349773unp87ps","5f","0
xf880bf164003ab0d"],"error":null}\n'
==> b'{"id": 12, "result": true, "error": null}\n'

==> b'{"id": 2876799, "method": "mining.notify", "params": ["3e", [5267937438567423666, 1402323897611195082, 977474031763684213
4, 440063524560526792], 1666417196923]}\n'
<== b'{"method":"mining.submit","id":13,"params":["kaspa:qrygml00m4v9wp4stz4875jxak457up20a78yuw8p20ytd9m349773unp87ps","3e","0
xf8809e55001a4d19"],"error":null}\n'
==> b'{"id": 13, "result": true, "error": null}\n'
.............
```
