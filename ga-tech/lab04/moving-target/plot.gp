set terminal pngcairo size 300,500 enhanced font 'Verdana,10'
set output 'aslr-pie.png'

set palette gray negative
set autoscale xfix
set autoscale yfix
set xtics 1
set ytics 1
set format y "%x"
set title "Distribution of pie addresses"

set tics scale 0,0.001
set mxtics 2
set mytics 2
set grid front mxtics mytics lw 1.5 lt -1 lc rgb 'white'

plot "data" matrix w image noti