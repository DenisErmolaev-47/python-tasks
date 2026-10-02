<html>
<head>
<title>566. Reshape the Matrix.py</title>
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
566. Reshape the Matrix.py</font>
</center></td></tr></table>
<pre><span class="s0">class </span><span class="s1">Solution</span><span class="s2">(</span><span class="s1">object</span><span class="s2">):</span>
    <span class="s0">def </span><span class="s1">matrixReshape</span><span class="s2">(</span><span class="s1">self</span><span class="s2">, </span><span class="s1">mat</span><span class="s2">, </span><span class="s1">r</span><span class="s2">, </span><span class="s1">c</span><span class="s2">):</span>
        <span class="s3">&quot;&quot;&quot; 
        :type mat: List[List[int]] 
        :type r: int 
        :type c: int 
        :rtype: List[List[int]] 
        &quot;&quot;&quot;</span>
        <span class="s1">m </span><span class="s2">= </span><span class="s1">len</span><span class="s2">(</span><span class="s1">mat</span><span class="s2">)</span>
        <span class="s1">n </span><span class="s2">= </span><span class="s1">len</span><span class="s2">(</span><span class="s1">mat</span><span class="s2">[</span><span class="s4">0</span><span class="s2">])</span>
        <span class="s0">if </span><span class="s1">m </span><span class="s2">* </span><span class="s1">n </span><span class="s2">!= </span><span class="s1">r </span><span class="s2">* </span><span class="s1">c</span><span class="s2">:</span>
            <span class="s0">return </span><span class="s1">mat</span>
        <span class="s1">flat_list </span><span class="s2">= [</span><span class="s1">num </span><span class="s0">for </span><span class="s1">row </span><span class="s0">in </span><span class="s1">mat </span><span class="s0">for </span><span class="s1">num </span><span class="s0">in </span><span class="s1">row</span><span class="s2">]</span>
        <span class="s1">reshaped_matrix </span><span class="s2">= []</span>
        <span class="s0">for </span><span class="s1">i </span><span class="s0">in </span><span class="s1">range</span><span class="s2">(</span><span class="s1">r</span><span class="s2">):</span>
            <span class="s1">row_slice </span><span class="s2">= </span><span class="s1">flat_list</span><span class="s2">[</span><span class="s1">i </span><span class="s2">* </span><span class="s1">c</span><span class="s2">: (</span><span class="s1">i </span><span class="s2">+ </span><span class="s4">1</span><span class="s2">) * </span><span class="s1">c</span><span class="s2">]</span>
            <span class="s1">reshaped_matrix</span><span class="s2">.</span><span class="s1">append</span><span class="s2">(</span><span class="s1">row_slice</span><span class="s2">)</span>

        <span class="s0">return </span><span class="s1">reshaped_matrix</span></pre>
</body>
</html>