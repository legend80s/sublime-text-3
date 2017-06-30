## PHP
.sublime-snippet

1. error_log.sublime-snippet

```xml
<snippet>
	<content><![CDATA[
error_log('$1: ' . json_encode($1, JSON_PRETTY_PRINT) . "\n");
]]></content>
	<!-- Optional: Set a tabTrigger to define how to trigger the snippet -->
	<tabTrigger>log</tabTrigger>
	<!-- Optional: Set a scope to limit where the snippet will trigger -->
	<scope>source.php</scope>
</snippet>
```

2. arrow
```xml
<snippet>
	<content><![CDATA[
->
]]></content>
	<!-- Optional: Set a tabTrigger to define how to trigger the snippet -->
	<tabTrigger>.</tabTrigger>
	<!-- Optional: Set a scope to limit where the snippet will trigger -->
	<scope>source.php</scope>
</snippet>
```

3. this

```xml
<snippet>
	<content><![CDATA[
\$this->
]]></content>
	<!-- Optional: Set a tabTrigger to define how to trigger the snippet -->
	<tabTrigger>this</tabTrigger>
	<!-- Optional: Set a scope to limit where the snippet will trigger -->
	<scope>source.php</scope>
</snippet>
```

4. json_encode
```xml
<snippet>
    <content><![CDATA[
json_encode($1, JSON_PRETTY_PRINT)
]]></content>
    <tabTrigger>hello</tabTrigger>
    <scope>source.php</scope>
</snippet>
```

5. error_log_basic
```xml
<snippet>
    <content><![CDATA[
error_log('$1');
]]></content>
    <tabTrigger>error_log</tabTrigger>
    <scope>source.php</scope>
</snippet>
```
