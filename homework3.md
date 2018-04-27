

### Question one

It is obviously a Markov Chain:



### Question two

> $r1 = 0.993\times (1-0.005 \times 0.005) \times (1-0.002 \times (1-0.99*0.999)) \times 0.98 \\ \times (1-(1-0.99 \times0.99) \times (1-0.99\times 0.99))r1 = 0.993 \times 0.999975 \times 0.99997802 \times 0.98 \times 0.99960399 = 0.9727$
>
> $r2 = 0.998\times (1-0.005 \times 0.005)\times(1-0.01\times0.001\times0.002)\times0.98 \\ \times(1-0.00000001)r2 = 0.998\times0.999975\times0.99999998\times0.98 \times 0.99999999 = 0.978$

The reliability of the second design is higher than the reliability of the first design. Also, forlanding and rockets the second alternative has more parallel options, so it is less likely to fail.The assumption encoded in the design is that the mission is successful whenever power,communication, landing, storage and rockets work properly (at least one of the correspondingcomponents when more are connected in parallel, more complex relation for landing in firstdesign). The less reasonable assumption is that the design has no impact on the parameters ofthe actual mission: the minimum number of rockets required for propulsion probably has animpact on the actual force that can be generated.

Note that the second design has better power supply. Even if we replace it with one of thesame quality (reliability $0.993$) the second design is still better, but the difference is reduced: $r2 = 0.9731$.



### Question three

Consider the data in the table in order to predict weight as a function of height. Let $x$ and $y$ represent the height and weight respectively.

| Height(in) $x$ | weight(lb) $y$ |
| :------------- | :------------- |
| 60             | 132            |
| 61             | 136            |
| 62             | 141            |
| 63             | 145            |
| 64             | 150            |
| 65             | 155            |
| 66             | 160            |
| 67             | 165            |
| 68             | 170            |
| 69             | 175            |
| 70             | 180            |
| 71             | 185            |
| 72             | 190            |
| 73             | 195            |
| 74             | 201            |
| 75             | 206            |
| 76             | 212            |
| 77             | 218            |
| 78             | 223            |
| 79             | 229            |
| 80             | 234            |

The objective is to find the linear model for best fit $y= ax +b$ 

The objective is to find the values of a$a$ and $b$ uses the formulas