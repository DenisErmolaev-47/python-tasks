<html>
<head>
<title>137. Single Number II.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #cf8e6d;}
.s1 { color: #bcbec4;}
.s2 { color: #bcbec4;}
.s3 { color: #5f826b; font-style: italic;}
.s4 { color: #2aacb8;}
</style>
</head>
<body bgcolor="#1e1f22">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#606060" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
137. Single Number II.py</font>
</center></td></tr></table>
<pre><span class="s0">class </span><span class="s1">Solution</span><span class="s2">(</span><span class="s1">object</span><span class="s2">):</span>
    <span class="s0">def </span><span class="s1">singleNumber</span><span class="s2">(</span><span class="s1">self</span><span class="s2">, </span><span class="s1">nums</span><span class="s2">):</span>
        <span class="s3">&quot;&quot;&quot; 
        :type nums: List[int] 
        :rtype: int 
        &quot;&quot;&quot;</span>
        <span class="s1">ones </span><span class="s2">= </span><span class="s4">0</span>
        <span class="s1">twos </span><span class="s2">= </span><span class="s4">0</span>
        <span class="s0">for </span><span class="s1">num </span><span class="s0">in </span><span class="s1">nums</span><span class="s2">:</span>
            <span class="s1">ones </span><span class="s2">= (</span><span class="s1">ones </span><span class="s2">^ </span><span class="s1">num</span><span class="s2">) &amp; ~</span><span class="s1">twos</span>
            <span class="s1">twos </span><span class="s2">= (</span><span class="s1">twos </span><span class="s2">^ </span><span class="s1">num</span><span class="s2">) &amp; ~</span><span class="s1">ones</span>

        <span class="s0">return </span><span class="s1">ones</span></pre>
</body>
</html>