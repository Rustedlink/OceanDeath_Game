<html>
<head>
<title>main.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #a9b7c6;}
.s1 { color: #6a8759;}
.s2 { color: #cc7832;}
</style>
</head>
<body bgcolor="#2b2b2b">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#606060" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
main.py</font>
</center></td></tr></table>
<pre><span class="s0">print(</span><span class="s1">'''                            ______________________________________________ 
                          .-'                     _                        '. 
                        .'                       |-'                        | 
                      .'                         |                          | 
                   _.'               p         _\_/_         p              | 
                _.'                  |       .'  |  '.       |              | 
           __..'                     |      /    |    \      |              | 
     ___..'                         .T\    ======+======    /T.             | 
  ;;;\::::                        .' | \  /      |      \  / | '.           | 
  ;;;|::::                      .'   |  \/       |       \/  |   '.         | 
  ;;;/::::                    .'     |   \       |        \  |     '.       | 
        ''.__               .'       |    \      |         \ |       '.     | 
             ''._          &lt;_________|_____&gt;_____|__________&gt;|_________&gt;    | 
                 '._     (___________|___________|___________|___________)  | 
                    '.    \;;;Dani;;;o;;;;;o;;;;;o;;;;;o;;;;;o;;;;;o;;;;/   | 
                      '.~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~   | 
                        '. ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~  | 
                          '-.______________________________________________.'''</span><span class="s0">)</span>


<span class="s0">print(</span><span class="s1">&quot;Welcome to Ocean Death&quot;</span><span class="s0">)</span>
<span class="s0">print(</span><span class="s1">&quot;Your mission is to survive&quot;</span><span class="s0">)</span>

<span class="s0">choice1 =  input(</span><span class="s1">&quot;Your boat is sinking and you are surounded by sharks. Swim 'left' or swim 'right'.</span><span class="s2">\n</span><span class="s1">&quot;</span><span class="s0">).lower()</span>
<span class="s2">if </span><span class="s0">choice1 == </span><span class="s1">&quot;left&quot;</span><span class="s0">:</span>
  <span class="s0">choice2 = input(</span><span class="s1">&quot;You swim to a small island but it full of zombies. You have decicion to either 'fight' or 'friend' the zombies.</span><span class="s2">\n </span><span class="s1">&quot;</span><span class="s0">).lower()</span>
  <span class="s2">if </span><span class="s0">choice2 == </span><span class="s1">&quot;fight&quot;</span><span class="s0">:</span>
    <span class="s0">choice3 = input(</span><span class="s1">&quot;You fought off the zombies and run in to a building there are three doors. One door say's 'Treasure' another says 'Death' the last door says 'Happiness' choose wisely.</span><span class="s2">\n</span><span class="s1">&quot;</span><span class="s0">).lower()</span>
    <span class="s2">if </span><span class="s0">choice3 == </span><span class="s1">&quot;treasure&quot;</span><span class="s0">:</span>
      <span class="s0">print(</span><span class="s1">&quot;Its called Ocean Death you lose...&quot;</span><span class="s0">)</span>
    <span class="s2">elif </span><span class="s0">choice3 == </span><span class="s1">&quot;death&quot;</span><span class="s0">:</span>
      <span class="s0">print(</span><span class="s1">&quot;You suck at games you lose...&quot;</span><span class="s0">)</span>
    <span class="s2">elif </span><span class="s0">choice3 == </span><span class="s1">&quot;happiness&quot;</span><span class="s0">:</span>
      <span class="s0">print(</span><span class="s1">&quot;Congrats you beat the game nerd!&quot;</span><span class="s0">)</span>
    <span class="s2">else</span><span class="s0">:</span>
      <span class="s0">print(</span><span class="s1">&quot;that door doesnt exist you lose&quot;</span><span class="s0">)</span>
  <span class="s2">else</span><span class="s0">:</span>
    <span class="s0">print(</span><span class="s1">&quot;Why would you try to be friends with a zombie you DIE!&quot;</span><span class="s0">)  </span>
<span class="s2">else</span><span class="s0">:</span>
  <span class="s0">print(</span><span class="s1">&quot;Congratulations you were eaten by sharks!&quot;</span><span class="s0">)</span></pre>
</body>
</html>
