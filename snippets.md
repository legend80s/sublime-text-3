## PHP
ext: .sublime-snippet

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

6. array_map
```xml
<snippet>
    <content><![CDATA[
array_map(function (\$$2) { return \$$3; }, $1);
]]></content>
    <tabTrigger>map</tabTrigger>
    <scope>source.php</scope>
</snippet>
```

7. array_filter
```xml
<snippet>
    <content><![CDATA[
array_filter(${1:input}, function ($2) { return $3; });
]]></content>
    <tabTrigger>filter</tabTrigger>
    <scope>source.js</scope>
</snippet>
```

8. self
```xml
<snippet>
    <content><![CDATA[
self::$1
]]></content>
    <tabTrigger>self</tabTrigger>
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

2. console.log-short
```xml
<snippet>
    <content><![CDATA[
console.log('$1');
]]></content>
    <tabTrigger>lo</tabTrigger>
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

4. key-value
```xml
<snippet>
    <content><![CDATA[
{
  ${1:key}: '${2:value}'

]]></content>
    <tabTrigger>{</tabTrigger>
    <scope>source.js</scope>
</snippet>

5. interpolation.sublime-snippet
```xml
<snippet>
    <content><![CDATA[
\${$1}
]]></content>
    <tabTrigger>s</tabTrigger>
    <scope>source.js</scope>
</snippet>
```

6. import
```xml
<snippet>
    <content><![CDATA[
import $1 from '$1';
]]></content>
    <tabTrigger>import</tabTrigger>
    <scope>source.js</scope>
</snippet>
```

7. import-member
```xml
<snippet>
    <content><![CDATA[
import { $1 } from '$2';
]]></content>
    <tabTrigger>import-member</tabTrigger>
    <scope>source.js</scope>
</snippet>
```

8. module-exports
```xml
<snippet>
    <content><![CDATA[
module.exports = $1;
]]></content>
    <tabTrigger>module.exports</tabTrigger>
    <scope>source.js</scope>
</snippet>
```

9. ng-inject
```xml
<snippet>
    <content><![CDATA[
\inject = ['$1'];
]]></content>
    <tabTrigger>inject</tabTrigger>
    <scope>source.js</scope>
</snippet>
```

10. arrow-function
```xml
<snippet>
    <content><![CDATA[
() => {}
]]></content>
    <tabTrigger>func</tabTrigger>
    <scope>source.js</scope>
</snippet>
```

11. undefined
```xml
<snippet>
    <content><![CDATA[
undefined
]]></content>
    <tabTrigger>undefined</tabTrigger>
    <scope>source.js</scope>
</snippet>
```

12. require
```xml
<snippet>
    <content><![CDATA[
const $1 = require('$1');
]]></content>
    <tabTrigger>require</tabTrigger>
    <scope>source.js</scope>
</snippet>
```

13. node_modules
```xml
<snippet>
    <content><![CDATA[
node_modules
]]></content>
    <tabTrigger>node_modules</tabTrigger>
    <scope>source.js</scope>
</snippet>
```

## Angular
1. rootScope
```xml
<snippet>
    <content><![CDATA[
rootScope
]]></content>
    <tabTrigger>rootScope</tabTrigger>
    <scope>source.js</scope>
</snippet>
```

## HTML

1. p-log
```xml
<snippet>
    <content><![CDATA[
<p>$1: {{ $1 }}</p>
]]></content>
    <tabTrigger>log</tabTrigger>
    <scope>text.html</scope>
</snippet>
```

## Shell
1. shebang
```xml
<snippet>
    <content><![CDATA[
#!/bin/bash

set -e
set -x

$1
]]></content>
    <tabTrigger>#!</tabTrigger>
    <scope>source.shell</scope>
</snippet>
```
