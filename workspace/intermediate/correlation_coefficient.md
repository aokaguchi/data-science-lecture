
## 相関係数の幾何的意味
---
サンプルサイズ $n$ の 2 変数データ、 $x_{1} ,x_{2} ,\dotsc ,x_{n}$ ・ $y_{1} ,y_{2} ,\dotsc ,y_{n}$ について、ベクトル $\boldsymbol{x},\boldsymbol{y}$ をそれぞれの偏差として以下のように定義する。

$
\begin{cases}
    \boldsymbol{x} =\left( x_{1} -\overline{x} ,x_{2} -\overline{x} ,\dotsc ,x_{n} -\overline{x}\right)\\
    \boldsymbol{y} =\left( y_{1} -\overline{y} ,y_{2} -\overline{y} ,\dotsc ,y_{n} -\overline{y}\right)
\end{cases}
$

このとき、ベクトル $\boldsymbol{x},\boldsymbol{y}$ のなす角度を $\theta$ とすると、相関係数 $r_{xy}=cos\theta$ となる。  
つまり、相関係数は 2 つのベクトルがどの程度同じ方向を向いているかを表す。

### 導出
---
内積の定義 $\displaystyle \boldsymbol{a} \cdot \boldsymbol{b} =\sum ^{n}_{i=1} a_{i} b_{i} =\| \boldsymbol{a} \| \ \| \boldsymbol{b} \| \ cos\theta $ より

$
\displaystyle \sum ^{n}_{i=1}\left( x_{i} -\overline{x}\right)\left( y_{i} -\overline{y}\right) =\sqrt{\sum ^{n}_{i=1}\left( x_{i} -\overline{x}\right)^{2}}\sqrt{\sum ^{n}_{i=1}\left( y_{i} -\overline{y}\right)^{2}} cos\theta
$

標準偏差 $S( x)$ ・共分散 $Cov( x,y)$ の定義

$
\begin{cases}
    S( x) & =\sqrt{
        \displaystyle \frac
            {1}
            {n}
        \sum ^{n}_{i=1}\left( x_{i} -\overline{x}\right)^{2}
    }\\
    Cov( x,y) & =\displaystyle \frac
        {1}
        {n}
    \sum ^{n}_{i=1}\left( x_{i} -\overline{x}\right)\left( y_{i} -\overline{y}\right)
\end{cases}
$

より

$
\displaystyle \begin{aligned}
    nCov( x,y) & =\sqrt{n} S( x)\sqrt{n} S( y) cos\theta \\
    cos\theta  & =\frac
        {Cov( x,y)}
        {S( x) S( y)}
\end{aligned}
$

相関係数 $
\displaystyle r_{xy} =\frac
    {Cov( x,y)}
    {S( x) S( y)}
$ より $r_{xy}=cos\theta$
