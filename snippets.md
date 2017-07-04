## PHP
.sublime-snippet

1. error_log.sublime-snippet

```xml
<snippet>
	<content><![CDATA[
error_log('$1: ' . json_encode($1, JSON_PRETTY_PRINT) . "\n");
]]></content>
	<tabTrigger>log</tabTrigger>
	<scope>source.php</scope>
</snippet>
```

2. arrow
```xml
<snippet>
	<content><![CDATA[
->
]]></content>
	<tabTrigger>.</tabTrigger>
	<scope>source.php</scope>
</snippet>
```

3. this

```xml
<snippet>
	<content><![CDATA[
\$this->
]]></content>
	<tabTrigger>this</tabTrigger>
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

## JavaScript
1. console.log-verbose.sublime-snippet
```xml
<snippet>
    <content><![CDATA[
console.log('$1:', $1);
]]></content>
    <tabTrigger>log</tabTrigger>
    <scope>source.js</scope>
</snippet>
```

2. return
```xml
<snippet>
    <content><![CDATA[
return ${1};
]]></content>
    <tabTrigger>return</tabTrigger>
    <scope>source.js</scope>
</snippet>
```

3. export-default
```xml
<snippet>
    <content><![CDATA[
export default $1;
]]></content>
    <tabTrigger>exp</tabTrigger>
    <scope>source.js</scope>
</snippet>
```
