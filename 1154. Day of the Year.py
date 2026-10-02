<html>
<head>
<title>1154. Day of the Year.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #cf8e6d;}
.s1 { color: #bcbec4;}
.s2 { color: #bcbec4;}
.s3 { color: #5f826b; font-style: italic;}
.s4 { color: #6aab73;}
.s5 { color: #2aacb8;}
</style>
</head>
<body bgcolor="#1e1f22">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#606060" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
1154. Day of the Year.py</font>
</center></td></tr></table>
<pre><span class="s0">class </span><span class="s1">Solution</span><span class="s2">(</span><span class="s1">object</span><span class="s2">):</span>
    <span class="s0">def </span><span class="s1">dayOfYear</span><span class="s2">(</span><span class="s1">self</span><span class="s2">, </span><span class="s1">date</span><span class="s2">):</span>
        <span class="s3">&quot;&quot;&quot; 
        :type date: str 
        :rtype: int 
        &quot;&quot;&quot;</span>
        <span class="s1">year</span><span class="s2">, </span><span class="s1">month</span><span class="s2">, </span><span class="s1">day </span><span class="s2">= </span><span class="s1">map</span><span class="s2">(</span><span class="s1">int</span><span class="s2">, </span><span class="s1">date</span><span class="s2">.</span><span class="s1">split</span><span class="s2">(</span><span class="s4">'-'</span><span class="s2">))</span>
        <span class="s1">days_in_month </span><span class="s2">= [</span><span class="s5">31</span><span class="s2">, </span><span class="s5">28</span><span class="s2">, </span><span class="s5">31</span><span class="s2">, </span><span class="s5">30</span><span class="s2">, </span><span class="s5">31</span><span class="s2">, </span><span class="s5">30</span><span class="s2">, </span><span class="s5">31</span><span class="s2">, </span><span class="s5">31</span><span class="s2">, </span><span class="s5">30</span><span class="s2">, </span><span class="s5">31</span><span class="s2">, </span><span class="s5">30</span><span class="s2">, </span><span class="s5">31</span><span class="s2">]</span>
        <span class="s1">is_leap_year </span><span class="s2">= (</span><span class="s1">year </span><span class="s2">% </span><span class="s5">400 </span><span class="s2">== </span><span class="s5">0</span><span class="s2">) </span><span class="s0">or </span><span class="s2">(</span><span class="s1">year </span><span class="s2">% </span><span class="s5">100 </span><span class="s2">!= </span><span class="s5">0 </span><span class="s0">and </span><span class="s1">year </span><span class="s2">% </span><span class="s5">4 </span><span class="s2">== </span><span class="s5">0</span><span class="s2">)</span>
        <span class="s0">if </span><span class="s1">is_leap_year</span><span class="s2">:</span>
            <span class="s1">days_in_month</span><span class="s2">[</span><span class="s5">1</span><span class="s2">] = </span><span class="s5">29</span>
        <span class="s0">return </span><span class="s1">sum</span><span class="s2">(</span><span class="s1">days_in_month</span><span class="s2">[:</span><span class="s1">month </span><span class="s2">- </span><span class="s5">1</span><span class="s2">]) + </span><span class="s1">day</span></pre>
</body>
</html>