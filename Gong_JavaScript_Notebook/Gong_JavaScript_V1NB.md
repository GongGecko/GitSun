# JavaScript学习笔记(Gong_JavaScript_V1NB)。

[TOC]

## 第01章(JavaScript教程)

@import "廖雪峰JavaScript教程001.jpg"

### 第01节(JavaScript简介)

@import "廖雪峰JavaScript教程002.jpg"

```JavaScript

// ECMA(European Computer Manufacturers Association)组织定制了JavaScript语言标准,称为ECMAScript标准。

// 最新版ECMAScript 6 标准(简称ES6)在2015年6月正式发布
// JavaScript版本实际上指ECMAScript标准的某个版本的实现

```

## 第02章(快速入门)

@import "廖雪峰JavaScript教程003.jpg"

```JavaScript

// JavaScript代码可以嵌在网页任何地方,通常放在<head>中;

<script src="file://C:/EDisk/BT_1/Python3Gong/HTM/hts2.js"></script>

// JS代码可以单独放入.js文件,多个页面可以引用同一份.js文件,同一个页面可以引用多个.js文件

<script type="text/javascript"></script>
// <script>标签,type属性,如上没有必要,默认type就是JavaScript

// 注意：不要用Word或写字板来编写JavaScript或HTML
// 浏览器运行JavaScript,要先有HTML页面
// 注释,以双斜杠开头直到行末
/* 同样是注释 */


// Chrome浏览器>>>开发者工具(Developer Tools)>>>控制台(Console)>>>输JavaScript代码,回车
var a=2*3+1;
console.log(a);

```

```html

<!--C:\EDisk\BT_1\Python3Gong\HTM\htmJ2.html-->
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>htmJ2 | 好小兆(haoxiaozhao.com)</title>
    <script src="file://C:/EDisk/BT_1/Python3Gong/HTM/hts2.js"></script>
</head>
<body>
    <h1>这是htmJ2.html文件</h1>
</body>
</html>

```

### 第01节(基本语法)

@import "廖雪峰JavaScript教程004.jpg"

```JavaScript

console.log('................................S001................................');
if (2 > 1) {
    x = 1;
    y = 2;
    z = 3;
    if (x < y) {
        z = 4;
    }
    if (x > y) {
        z = 5;
    }
}
console.log('................................S001................................');

// 花括号{...}内语句具有缩进,通常4个空格;{...}可以嵌套,形成层级结构;

// 行注释

/* 块注释
仍然是注释
仍然是注释
注释结束 */

// JavaScript严格区分大小写

```

### 第02节(数据类型和变量)

#### 第01条(数据类型)

@import "廖雪峰JavaScript教程005.jpg"

```JavaScript

// JS不区分整数和浮点数,以下都是合法Number类型

123; // 整数123
0.456; // 浮点数0.456
1.2345e3; // 科学计数法表示1234.5
-99; // 负数
NaN; // NaN(Not a Number),无法计算结果时用NaN表示
Infinity; // Infinity表示无限大,当数值超过Number所能表示的最大值时表示


(1 + 2) * 5 / 2; // 7.5
2 / 0; // Infinity
0 / 0; // NaN
10 % 3; // 1
10.5 % 3; // 1.5
// %是求余运算


// 字符串是以单引号'或双引号"括起来的任意文本


true; // 布尔值,只有true、false两种值
false; // false
2 > 1; // true
2 >= 3; // false


// &&运算,与运算;||运算,或运算;!运算,非运算;

true && true; // true
true && false; // false
false || false; // false
true || false; // true
false || true || false; // true
! true; // false
! false; // true
! (2 > 5); // true


2 > 5; // false
5 >= 2; // true
7 == 7; // true
false == 0; // true
false === 0; // false

// 比较运算符,不要使用==比较,始终坚持使用===比较
// 第一种==比较,自动转换数据类型再比较,很多时候会得到诡异结果；
// 第二种===比较,不会自动转换数据类型,如果数据类型不一致,返回false,如果一致,再比较。

NaN === NaN; // false
// NaN与所有值都不相等,包括自己

isNaN(NaN); // true
// isNaN()函数,唯一能判断NaN的方法

1/3===(1-2/3); // false
Math.abs(1/3-(1-2/3))<0.0000001; // true
// 比较浮点数是否相等,通过计算是否小于某个阈值


// null表示一个“空”的值,undefined表示值“未定义”。区分两者意义不大,多数情况用null,undefined判断函数参数是否传递。


// 数组是一组按顺序排列的集合,集合的每个值称为元素(包含任意数据类型)。
[1, 2, 3.14, 'Hello', null, true];

new Array(1, 2, 3); // 创建数组[1, 2, 3]
// Array()函数也可以创建数组,但出于代码可读性考虑,强烈建议直接使用[]。


var arr = [1, 2, 3.14, 'Hello', null, true];
arr[0]; // 返回索引为0的元素,即1
arr[5]; // 返回索引为5的元素,即true
arr[6]; // 索引超出了范围,返回undefined


// 对象是一组由键-值组成的无序集合

var person = {
    name: 'Bob',
    age: 20,
    tags: ['js', 'web', 'mobile'],
    city: 'Beijing',
    hasCar: true,
    zipcode: null
};

// 对象的键都是字符串类型,值可以是任意数据类型。每个键称为对象的属性,person的name属性为'Bob',zipcode属性为null。

person.name; // 'Bob'
person.zipcode; // null

```

#### 第02条(变量)

@import "廖雪峰JavaScript教程014.jpg"

```JavaScript

// 变量名由大小写英文、数字、$和_组成,且不能数字开头。申明一个变量用var语句。
// 变量名可以中文,但请不要给自己找麻烦。

var a; // 申明变量a,此时a的值为undefined
var $b = 1; // 申明变量$b,同时给$b赋值
var s_007 = '007'; // s_007是字符串
var Answer = true; // Answer是布尔值
var t = null;

var a = 123; // a值是整数
a = 'ABC'; // a值是字符串
// 只需用var申明一次

var x = 100;
console.log(x);
// console.log(x),显示变量内容;Chrome控制台(Console)中查看。

var x = 100;
alert(x);
// 弹出对话框中显示;console.log(x)方式较清爽。



i=10; // 没有通过var申明,该变量自动被申明为全局变量

// strict模式,强制通过var申明变量,否则将导致运行错误
// 启用strict模式,在JS代码第一行写上：
'use strict';
// 此为字符串,不支持strict模式浏览器会按字符串语句执行,支持strict模式浏览器将开启strict模式运行JS。


'use strict';
// 如果浏览器支持strict模式,下面代码将报ReferenceError错误
abc='Hello, world'; // (Chrome),Uncaught ReferenceError: abc is not defined
console.log(abc);

```

### 第03节(字符串)

@import "廖雪峰JavaScript教程006.jpg"

```JavaScript

'I\'m \"OK\"!';
'\x41'; // ASCII字符,\x##,十六进制,等同于 'A'
'\u4e2d\u6587'; // Unicode字符,\u####,十六进制,等同于 '中文'


// 多行字符串,用反引号包围

`这是多行
字符串用
反引号包围`;


// 浏览器不支持ES6,报SyntaxError错误
console.log(`多行
字符串
测试`);

// 改写,反引号换成单引号
console.log('多行\n字符串\n测试');



var name = '小明';
var age = 20;
var message = '你好, ' + name + ', 你今年' + age + '岁了!';
alert(message);
// 你好, 小明, 你今年20岁了!

var name = '小明';
var age = 20;
var message = `你好, ${name}, 你今年${age}岁了!`; // 模板字符串,ES6
alert(message);
// 你好, 小明, 你今年20岁了!


var s = 'Hello, world!';
s.length; // 13


var s = 'Hello, world!';

s[0]; // 'H'
s[6]; // ' '
s[7]; // 'w'
s[12]; // '!'
s[13]; // 超出范围不会报错,返回 undefined


var s = 'Test';
s[0] = 'X';
console.log(s[0]); // 'T'
console.log(s); // 'Test',字符串不可变


var s = 'Hello';
s.toUpperCase(); // 'HELLO'
// 不改变原有字符串,而是返回一个新字符串
// toUpperCase(),字符串全部变为大写

var s = 'Hello';
var lower = s.toLowerCase();
console.log(lower); // 'hello'
// toLowerCase(),字符串全部变为小写

var s = 'hello, world';
s.indexOf('world'); // 7
s.indexOf('World'); // 没有找到指定的子串,返回-1
// indexOf(),搜索指定字符串索引

var s = 'hello, world'
s.substring(0, 5); // 从索引0开始到5(不包括5),返回 'hello'
s.substring(7); // 从索引7开始到结束,返回 'world'
// substring(),返回指定索引区间的子串

```

### 第04节(数组)

@import "廖雪峰JavaScript教程007.jpg"

```JavaScript

var arr = [1, 2, 3.14, 'Hello', null, true];
arr.length; // 6


var arr = [1, 2, 3];
arr.length; // 3
arr.length = 6; // 重要,赋值给length会导致Array大小变化
arr; // [1, 2, 3, undefined, undefined, undefined]
arr.length = 2;
arr; // [1, 2]


var arr = ['A', 'B', 'C'];
arr[1] = 99;
arr; // ['A', 99, 'C']


var arr = [1, 2, 3];
arr[5] = 'x';
arr; // [1, 2, 3, undefined, undefined, 'x']
// 其他编程语言越界访问索引会报错,JavaScript不会有任何错误,但不建议直接修改Array大小。


var arr = [10, 20, '30', 'xyz'];
arr.indexOf(10); // 元素10的索引为0
arr.indexOf(20); // 元素20的索引为1
arr.indexOf(30); // 元素30没有找到,返回-1
arr.indexOf('30'); // 元素'30'的索引为2


var arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G'];
arr.slice(0, 3); // ['A', 'B', 'C']
arr.slice(3); // ['D', 'E', 'F', 'G']
// slice(),对应String的substring(),返回一个新Array
var aCopy = arr.slice(); // slice()无参数,截取全部元素
console.log(aCopy); // ["A", "B", "C", "D", "E", "F", "G"]
console.log(aCopy === arr); // false
console.log(aCopy === ["A", "B", "C", "D", "E", "F", "G"]); // false


var arr = [1, 2];
arr.push('A', 'B'); // 返回Array新长度 4
// push(),向末尾添加若干元素
arr; // [1, 2, 'A', 'B']
arr.pop(); // 返回'B'
// pop(),删除最后一个元素
arr; // [1, 2, 'A']
arr.pop(); arr.pop(); arr.pop(); // 连续pop 3次
arr; // []
arr.pop(); // 空数组pop不报错,返回undefined
arr; // []


var arr = [1, 2];
arr.unshift('A', 'B'); // 返回Array新长度 4
// unshift(),往头部添加若干元素
arr; // ['A', 'B', 1, 2]
arr.shift(); // 返回'A'
// shift(),删除第一个元素
arr; // ['B', 1, 2]
arr.shift(); arr.shift(); arr.shift(); // 连续shift 3次
arr; // []
arr.shift(); // 空数组shift不报错,返回undefined
arr; // []


var arr = ['B', 'C', 'A'];
arr.sort();
arr; // ['A', 'B', 'C']
// sort()对当前Array排序,会改变原Array


var arr = ['one', 'two', 'three'];
arr.reverse(); 
arr; // ['three', 'two', 'one']
// reverse(),反转整个Array


var arr = ['Microsoft', 'Apple', 'Yahoo', 'AOL', 'Excite', 'Oracle'];
// 从索引2开始删除3个元素,然后再添加两个元素:
arr.splice(2, 3, 'Google', 'Facebook'); // 返回删除的元素 ['Yahoo', 'AOL', 'Excite']
arr; // ['Microsoft', 'Apple', 'Google', 'Facebook', 'Oracle']
// 只删除,不添加:
arr.splice(2, 2); // ['Google', 'Facebook']
arr; // ['Microsoft', 'Apple', 'Oracle']
// 只添加,不删除:
arr.splice(2, 0, 'Google', 'Facebook'); // 返回[],因为没有删除任何元素
arr; // ['Microsoft', 'Apple', 'Google', 'Facebook', 'Oracle']
// splice()方法是修改Array的“万能方法”
// 从指定的索引开始删除若干元素,再从该位置添加若干元素


var arr = ['A', 'B', 'C'];
var added = arr.concat([1, 2, 3]);
added; // ['A', 'B', 'C', 1, 2, 3]
arr; // ['A', 'B', 'C']
// concat()方法把当前Array与另一个Array连接,并返回一个新Array

var arr = ['A', 'B', 'C'];
arr.concat(1, 2, [3, 4]); // ['A', 'B', 'C', 1, 2, 3, 4]
// concat()方法接收任意元素和Array,并自动把Array拆开,添加到新Array


var arr = ['A', 'B', 'C', 1, 2, 3];
arr.join('-'); // 'A-B-C-1-2-3'
// join()方法把当前Array元素用指定字符串连接,返回新字符串
// 如果Array元素不是字符串,自动转换为字符串后再连接


var arr = [[1, 2, 3], [400, 500, 600], '-'];
// 多维数组


'use strict';
var arr = ['小明', '小红', '大军', '阿黄'];
console.log(`欢迎${arr[0]},${arr[1]},${arr[2]}和${arr[3]}同学！`);
// 欢迎小明,小红,大军和阿黄同学！

```

### 第05节(对象)

@import "廖雪峰JavaScript教程008.jpg"

```JavaScript

var xiaohong = {
    name: '小红',
    'middle-school': 'No.1 Middle School'
};

// 属性名包含特殊字符,用''括起来

xiaohong['middle-school']; // 'No.1 Middle School'
xiaohong['name']; // '小红'
xiaohong.name; // '小红'
// 编写JS代码时,属性名尽量使用标准变量名,通过object.prop的形式访问。

console.log('................................S002................................');
var xiaoming = {
    name: '小明'
};
xiaoming.age; // undefined
xiaoming.age = 18; // 新增age属性
xiaoming.age; // 18
delete xiaoming.age; // 删除age属性
xiaoming.age; // undefined
delete xiaoming['name']; // 删除name属性
xiaoming.name; // undefined
delete xiaoming.school; // 删除不存在的school属性也不会报错
// 访问不存在的属性不报错,返回undefined
console.log('................................S002................................');


console.log('................................S003................................');
var xiaoming = {
    name: '小明',
    birth: 1990,
    school: 'No.1 Middle School',
    height: 1.70,
    weight: 65,
    score: null
};

'name' in xiaoming; // true
'grade' in xiaoming; // false
// 用in操作符,检测是否拥有某一属性

'toString' in xiaoming; // true
// 属性存在,有可能是继承得到的
console.log('................................S003................................');

var xiaoming = {
    name: '小明'
};
xiaoming.hasOwnProperty('name'); // true
xiaoming.hasOwnProperty('toString'); // false
// hasOwnProperty()方法,判断属性是否是自身拥有的
console.log('................................S003................................');

```

### 第06节(条件判断)

@import "廖雪峰JavaScript教程009.jpg"

```JavaScript

var age = 20;
if (age >= 18)
    alert('adult');
// else语句可选;
// 语句块只包含一条语句,可以省略{};建议:永远写上{}。

// JS把null、undefined、0、NaN、空字符串''视为false,其他一概视为true。

console.log('................................S004................................');
'use strict';

var height = parseFloat(prompt('请输入身高(m):'));
var weight = parseFloat(prompt('请输入体重(kg):'));
var bmi = weight / (height ** 2);
var res;
if (bmi <= 18.5) {
    res = "过轻";
} else if (bmi > 18.5 && bmi <= 25) {
    res = "正常";
} else if (bmi > 25 && bmi <= 28) {
    res = "过重";
} else if (bmi > 28 && bmi <= 32) {
    res = "肥胖";
} else {
    res = "严重肥胖";
}
console.log(`身高: ${height}, 体重: ${weight}, BMI指数: ${bmi}, 结论: ${res}！`);
console.log('................................S004................................');

```

### 第07节(循环)

@import "廖雪峰JavaScript教程010.jpg"

```JavaScript

// for循环,通过初始条件、结束条件、递增条件来循环执行语句块

var x = 0;
var i;
for (i=1; i<=10000; i++) {
    x = x + i;
}
x; // 50005000


// 索引遍历数组
var arr = ['Apple', 'Google', 'Microsoft'];
var i, x;
for (i=0; i<arr.length; i++) {
    x = arr[i];
    console.log(x);
}



var x = 0;
for (;;) { // for循环3个条件都可以省略,将无限循环
    if (x > 100) {
        break; // break语句退出循环,否则就是死循环
    }
    x ++;
}
console.log(x); // 101


console.log('................................S005................................');
// for循环变体:for...in循环
var o = {
    name: 'Jack',
    age: 20,
    city: 'Beijing'
};
for (var key in o) {
    if (o.hasOwnProperty(key)) { // 过滤继承的属性
        console.log(key); // 'name', 'age', 'city'
    }
}
console.log('................................S005................................');

// Array对象的索引视为对象的属性
var a = ['A', 'B', 'C'];
for (var i in a) {
    console.log(i); // '0', '1', '2'
    console.log(a[i]); // 'A', 'B', 'C'
}
// 返回是String不是Number
console.log('................................S005................................');


console.log('................................S006................................');
// while循环
var x = 0;
var n = 99;
while (n > 0) {
    x = x + n;
    n = n - 2;
}
x; // 2500
console.log('................................S006................................');

// do...while循环,每次循环完成后判断条件,循环体至少执行1次
var n = 0;
do {
    n = n + 1;
} while (n < 100);
n; // 100
console.log('................................S006................................');


console.log('................................S007................................');
'use strict';

var arr = ['Bart', 'Lisa', 'Adam'];
while (arr.length) { // 正序
    console.log(`Hello, ${arr.shift()}!`);
}
arr = ['Bart', 'Lisa', 'Adam'];
while (arr.length) { // 倒序
    console.log(`Hello, ${arr.pop()}!`);
}
console.log('................................S007................................');

```

### 第08节(Map和Set)

@import "廖雪峰JavaScript教程011.jpg"

```JavaScript

// Map和Set是ES6标准新增的数据类型,根据浏览器支持情况使用

'use strict';
var m = new Map();
var s = new Set();
console.log('你的浏览器支持Map和Set！');
// 如果浏览器报ReferenceError错误,说明不支持,QQ浏览器10.4不支持


var m = new Map([['Michael', 95], ['Bob', 75], ['Tracy', 85]]);
m.get('Michael'); // 95
// 初始化Map需要一个二维数组,或者初始化一个空Map

var m = new Map(); // 空Map
m.set('Adam', 67); // 添加新的key-value
m.set('Bob', 59);
m.has('Adam'); // 是否存在key,true
m.get('Adam'); // 67
m.delete('Adam'); // 删除key
m.get('Adam'); // undefined
m.set('Tom', 67);
m.set('Tom', 88);
m.get('Tom'); // 88



var s1 = new Set(); // 空Set
var s2 = new Set([1, 2, 3]);
s2; // Set(3) {1, 2, 3}
// 初始化Set需要一个Array,或者初始化一个空Set


var s = new Set([1, 2, 3, 3, '3']);
s; // Set {1, 2, 3, "3"}
// Set自动过滤重复元素
s.add(4);
s; // Set(5) {1, 2, 3, "3", 4}
// add(key)方法,添加元素到Set中
s.delete(3);
s; // Set(4) {1, 2, "3", 4}
// delete(key)方法,删除元素

```

### 第09节(iterable)

@import "廖雪峰JavaScript教程012.jpg"

```JavaScript

// ES6标准引入新的iterable类型,Array、Map和Set都属于iterable类型。
// iterable类型的集合可以通过新的for...of循环来遍历。

console.log('................................S008................................');
var a = ['A', 'B', 'C'];
var s = new Set(['A', 'B', 'C']);
var m = new Map([[1, 'x'], [2, 'y'], [3, 'z']]);
for (var x of a) { // 遍历Array
    console.log(x);
}
for (var x of s) { // 遍历Set
    console.log(x);
}
for (var x of m) { // 遍历Map
    console.log(x[0] + '=' + x[1]);
}

/*
A
B
C
A
B
C
1=x
2=y
3=z
*/
console.log('................................S008................................');


console.log('................................S009................................');
// for...in循环由于历史遗留问题,遍历的实际上是对象的属性名称。
var a = ['A', 'B', 'C'];
a.name = 'Hello';
for (var x in a) {
    console.log(x); // '0', '1', '2', 'name'
}
console.log('................................S009................................');

// for...of循环完全修复了这些问题
var a = ['A', 'B', 'C'];
a.name = 'Hello';
for (var x of a) {
    console.log(x); // 'A', 'B', 'C'
}
console.log('................................S009................................');


console.log('................................S010................................');
// forEach方法,iterable内置,接收一个函数,每次迭代自动回调该函数。forEach(),ES5.1标准。
'use strict';
var a = ['A', 'B', 'C'];
a.forEach(function (element, index, array) {
    // element: 指向当前元素的值;index: 指向当前索引;array: 指向Array对象本身
    console.log(element + ', index = ' + index);
});

/*
A, index = 0
B, index = 1
C, index = 2
*/
console.log('................................S010................................');


console.log('................................S011................................');
// Set没有索引,回调函数前两参数是元素本身
var s = new Set(['A', 'B', 'C']);
s.forEach(function (element, sameElement, set) {
    console.log(element); // 'A', 'B', 'C'
});
console.log('................................S011................................');


console.log('................................S012................................');
'use strict';

// Map回调函数参数依次为value、key和map本身
var m = new Map([
    [1, 'x'],
    [2, 'y'],
    [3, 'z']
]);
m.forEach(function (value, key, map) {
    console.log(key + "-" + value);
});

/*
1-x
2-y
3-z
*/

m.forEach(function (value, key, map) {
    console.log(key); // '1', '2', '3'
});

m.forEach(function (key, map) { // 不要求参数统一
    console.log(key); // 'x', 'y', 'z'
});

m.forEach(function (value, map) {
    console.log(value); // 'x', 'y', 'z'
});

m.forEach(function (vw, kh) {
    console.log(kh); // '1', '2', '3'
});

m.forEach(function (as, er, yt) {
    console.log(yt);
});

/*
Map(3) {1 => "x", 2 => "y", 3 => "z"}
Map(3) {1 => "x", 2 => "y", 3 => "z"}
Map(3) {1 => "x", 2 => "y", 3 => "z"}
*/


var a = ['A', 'B', 'C'];
a.forEach(function (element) { // 不要求参数统一
    console.log(element); // 'A', 'B', 'C'
});
console.log('................................S012................................');

```

## 第03章(函数)

@import "廖雪峰JavaScript教程013.jpg"

### 第01节(函数定义和调用)

#### 第01条(定义函数、调用函数、arguments)

@import "廖雪峰JavaScript教程015.jpg"

```JavaScript

function abs(x) {
    if (x >= 0) {
        return x; // 一旦执行到return,函数执行完毕;没有return,结果返回undefined。
    } else {
        return -x;
    }
}


// 函数也是一个对象,函数名abs可以视为指向该函数的变量。
var abs = function (x) { // 此function (x)为匿名函数
    if (x >= 0) {
        return x;
    } else {
        return -x;
    }
};
// 上述两种定义完全等价,第二种注意加;,表示赋值语句结束


// JavaScript允许传入任意个参数而不影响调用
abs(10, 'blablabla'); // 返回10
abs(-9, 'haha', 'hehe', null); // 返回9
abs(); // 返回NaN,传入参数比定义少也不影响,abs(x)函数参数收到undefined,计算结果为NaN


function abs(x) {
    if (typeof x !== 'number') { // 参数检查
        throw 'Not a number';
    }
    if (x >= 0) {
        return x;
    } else {
        return -x;
    }
}

console.log('................................S013................................');
// 关键字arguments只在函数内部起作用,并且永远指向当前函数调用者传入的所有参数。
// arguments类似Array但它不是一个Array。

'use strict';
function foo(x) {
    console.log('x = ' + x);
    for (var i=0; i<arguments.length; i++) {
        console.log('arg ' + i + ' = ' + arguments[i]);
    }
}
foo(10, 20, 30);

/*
x = 10
arg 0 = 10
arg 1 = 20
arg 2 = 30
*/
console.log('................................S013................................');

function abs() { // 函数不定义参数,仍能得到参数值
    if (arguments.length === 0) {
        return 0;
    }
    var x = arguments[0];
    return x >= 0 ? x : -x;
}

abs(); // 0
abs(10); // 10
abs(-9); // 9
console.log('................................S013................................');

```

#### 第02条(rest参数)

@import "廖雪峰JavaScript教程016.jpg"

```JavaScript

function foo(a, b, ...rest) { // rest参数写在最后,前面用...标识,ES6标准
    console.log('a = ' + a);
    console.log('b = ' + b);
    console.log(rest);
}
foo(1, 2, 3, 4, 5); // 多余参数以数组形式交给变量rest
// a = 1
// b = 2
// Array [ 3, 4, 5 ]
foo(1); // 注意:rest参数接收一个空数组,不是undefined。
// a = 1
// b = undefined
// Array []


console.log('................................S014................................');
'use strict';

function sum(...rest) {
    var summ = 0;
    for (let n = 0; n < rest.length; n++) {
        summ += rest[n];
    }
    return summ;
}

// 测试:
var i, args = [];
for (i = 1; i <= 100; i++) {
    args.push(i);
}
if (sum() !== 0) {
    console.log('测试失败: sum() = ' + sum());
} else if (sum(1) !== 1) {
    console.log('测试失败: sum(1) = ' + sum(1));
} else if (sum(2, 3) !== 5) {
    console.log('测试失败: sum(2, 3) = ' + sum(2, 3));
} else if (sum.apply(null, args) !== 5050) {
    console.log('测试失败: sum(1, 2, 3, ..., 100) = ' + sum.apply(null, args));
} else {
    console.log('测试通过!');
}
console.log('................................S014................................');


console.log('................................S015................................');
function foo() {
    return { name: 'foo' };
}

foo(); // {name: "foo"}
console.log('................................S015................................');

// JavaScript引擎在行末自动添加分号
function foo() {
    return
    { name: 'foo' };
}

foo(); // undefined
console.log('................................S015................................');

// 同上
function foo() {
    return; // 自动添加分号,相当于return undefined;
    { name: 'foo' }; // 这行语句永远没法执行
}
console.log('................................S015................................');

// 正确的多行写法
function foo() {
    return { // 不会加分号,{表示语句尚未结束
        name: 'foo'
    };
}

foo();  // {name: "foo"}
console.log('................................S015................................');


console.log('................................S016................................');
'use strict';
// 计算圆面积
function area_of_circle(r, pi) {
    return arguments.length === 2 ? pi * r ** 2 : 3.14 * r ** 2;
}

// 测试:
if (area_of_circle(2) === 12.56 && area_of_circle(2, 3.1416) === 12.5664) {
    console.log('测试通过');
} else {
    console.log('测试失败');
}
console.log('................................S016................................');

```

### 第02节(变量作用域与解构赋值)

#### 第01条(变量作用域)

@import "廖雪峰JavaScript教程017.jpg"

```JavaScript

console.log('................................S017................................');
'use strict';

function foo() {
    var x = 1; // 变量在函数体内部申明,该变量的作用域为整个函数体
    x = x + 1;
}
x = x + 2; // ReferenceError! 无法在函数体外引用变量x
console.log('................................S017................................');

// 不同函数内部的同名变量互相独立,互不影响
// 由于JavaScript函数可以嵌套,内部函数可以访问外部函数定义的变量,反过来则不行
'use strict';

function foo() {
    var x = 1;
    function bar() {
        var y = x + 1; // bar可以访问foo的变量x!
    }
    var z = y + 1; // ReferenceError! foo不可以访问bar的变量y!
}
// 查找变量从“内”向“外”查找,如果内部函数与外部函数变量重名,则内部变量将“屏蔽”外部变量。
console.log('................................S017................................');


console.log('................................S018................................');
'use strict';

function foo() {
    var x = 'Hello, ' + y; // strict模式,但不报错,原因是变量提升
    console.log(x);
    var y = 'Bob';
}
foo(); // Hello, undefined
// JavaScript引擎自动提升变量y的申明,但不会提升变量y的赋值。
console.log('................................S018................................');

'use strict';
// 上述,相当于JavaScript引擎:
function foo() {
    var y; // 提升变量y的申明,此时y为undefined
    var x = 'Hello, ' + y;
    console.log(x);
    y = 'Bob';
}
console.log('................................S018................................');

// 故函数内部定义变量,首先申明所有变量。最常见用一个var申明函数内部用到的所有变量
function foo() {
    var
        x = 1,
        y = x + 1,
        z, i; // z和i为undefined
    for (i=0; i<3; i++) {
        z = x + y + i;
    }
    return z;
}
foo(); // 5
console.log('................................S018................................');


console.log('................................S019................................');
// 不在函数内定义的变量具有全局作用域。
// JavaScript默认有一个全局对象window,全局作用域的变量实际上被绑定到window的一个属性。

'use strict';

var course = 'Learn JavaScript';
alert(course); // 'Learn JavaScript'
alert(window.course); // 'Learn JavaScript',两者完全一致
console.log('................................S019................................');

// 以变量方式定义函数:var foo = function () {}也是一个全局变量

'use strict';

function foo() { // 顶层函数的定义也被视为一个全局变量,并绑定到window对象
    alert('foo');
}

foo();
window.foo(); // 两者完全一致
console.log('................................S019................................');

'use strict';

window.alert('调用window.alert()'); // alert()函数
// 把alert保存到另一个变量:
var old_alert = window.alert;
// 给alert赋一个新函数:
window.alert = function () { }
alert('无法用alert()显示了!');
// 恢复alert:
window.alert = old_alert;
alert('又可以用alert()了!');
console.log('................................S019................................');


console.log('................................S020................................');
// 全局变量绑定window,不同的JavaScript文件使用相同的全局变量,或定义相同名字的顶层函数,都会造成命名冲突。
// 减少冲突的方法是把所有变量和函数全部绑定到一个全局变量中。


// 唯一的全局变量MYAPP:
var MYAPP = {}; // 名字空间

// 其他变量:
MYAPP.name = 'myapp';
MYAPP.version = 1.0;

// 其他函数:
MYAPP.foo = function () {
    return 'foo';
};

alert(window.MYAPP.name);
alert(window.MYAPP.foo);
alert(window.MYAPP.foo());
console.log('................................S020................................');


console.log('................................S021................................');
'use strict';

function foo() {
    for (var i=0; i<100; i++) { // for循环等语句块,var无法定义具有局部作用域的变量
        i;
    }
    i += 100; // 变量i作用域实际上是函数内部
}
console.log('................................S021................................');

'use strict';

function foo() {
    var sum = 0;
    for (let i=0; i<100; i++) { // 块级作用域,用let替代var申明,ES6
        sum += i;
    }
    i += 1; // SyntaxError
}
console.log('................................S021................................');


var PI = 3.14; // ES6之前申明常量,通常用全部大写变量来表示


'use strict';
const PI = 3.14; // 关键字const定义常量,const与let都具有块级作用域,ES6
PI = 3; // 某些浏览器不报错,但是无效果！
PI; // 3.14

```

#### 第02条(解构赋值)

@import "廖雪峰JavaScript教程018.jpg"

```JavaScript

'use strict';

var [x, y, z] = ['hello', 'JavaScript', 'ES6']; // 解构赋值,用[...]括起来,ES6
console.log('x = ' + x + ', y = ' + y + ', z = ' + z);
// x = hello, y = JavaScript, z = ES6


let [x, [y, z]] = ['hello', ['JavaScript', 'ES6']]; // 嵌套层次和位置保持一致
let [, , z] = ['hello', 'JavaScript', 'ES6']; // 忽略前两个元素,只对z赋值

console.log('................................S022................................');
'use strict';

var person = {
    name: '小明',
    age: 20,
    gender: 'male',
    passport: 'G-12345678',
    school: 'No.4 middle school'
};
var { name, age, passport } = person;
console.log('name = ' + name + ', age = ' + age + ', passport = ' + passport);
// name = 小明, age = 20, passport = G-12345678
console.log('................................S022................................');

var person = {
    name: '小明',
    age: 20,
    gender: 'male',
    passport: 'G-12345678',
    school: 'No.4 middle school',
    address: { // 嵌套
        city: 'Beijing',
        street: 'No.1 Road',
        zipcode: '100001'
    }
};
var {name, address: {city, zip}} = person;
console.log(name); // '小明'
console.log(city); // 'Beijing'
console.log(zip); // undefined,属性名是zipcode不是zip
// address不是变量,是为了让city和zip获得嵌套的address对象的属性
console.log(address); // Uncaught ReferenceError: address is not defined
console.log('................................S022................................');


console.log('................................S023................................');
var person = {
    name: '小明',
    age: 20,
    gender: 'male',
    passport: 'G-12345678',
    school: 'No.4 middle school'
};

let {name, passport:id} = person;
console.log(name); // '小明'
console.log(id); // 'G-12345678'
// passport不是变量,是为了让变量id获得passport属性
console.log(passport); // Uncaught ReferenceError: passport is not defined
console.log('................................S023................................');

// 解构赋值可以使用默认值,避免属性不存在返回undefined。
var person = {
    name: '小明',
    age: 20,
    gender: 'male',
    passport: 'G-12345678'
};

// 如果person对象没有single属性,默认赋值为true
var {name, single=true} = person;
console.log(name); // '小明'
console.log(single); // true
console.log('................................S023................................');


var x, y;
{x, y} = { name: '小明', x: 100, y: 200};
// Uncaught SyntaxError: Unexpected token =
// JS把{开头的语句当作块处理,于是=不合法
({x, y} = { name: '小明', x: 100, y: 200}); // 用小括号括起来



var x=1, y=2;
[x, y] = [y, x]; // 解构赋值,交换两个变量的值


var {hostname:domain, pathname:path} = location; // 快速获取当前页面的域名和路径

console.log('................................S024................................');
function buildDate({year, month, day, hour=0, minute=0, second=0}) {
    return new Date(year + '-' + month + '-' + day + ' ' + hour + ':' + minute + ':' + second);
}

buildDate({ year: 2017, month: 1, day: 1 });
// Sun Jan 01 2017 00:00:00 GMT+0800 (CST)
buildDate({ year: 2017, month: 1, day: 1, hour: 20, minute: 15 });
// Sun Jan 01 2017 20:15:00 GMT+0800 (CST)
console.log('................................S024................................');

```

### 第03节(方法)

@import "廖雪峰JavaScript教程019.jpg"

```JavaScript

console.log('................................S025................................');
// 在一个对象中绑定函数,称为这个对象的方法
var xiaoming = {
    name: '小明',
    birth: 1990,
    age: function () { // age()方法
        var y = new Date().getFullYear();
        return y - this.birth;
    } // 在一个方法内部,this是一个特殊变量,它始终指向当前对象,也就是xiaoming这个变量。
};

console.log(xiaoming.age); // function xiaoming.age()
console.log(xiaoming.age()); // 今年调用29,明年调用30
console.log('................................S025................................');


console.log('................................S026................................');
function getAge() {
    var y = new Date().getFullYear();
    return y - this.birth;
}

var xiaoming = {
    name: '小明',
    birth: 1990,
    age: getAge
};

xiaoming.age(); // 29,正常结果
getAge(); // NaN
// 以对象的方法形式调用,比如xiaoming.age(),该函数的this指向被调用的对象
// 单独调用函数,比如getAge(),该函数的this指向全局对象,也就是window
console.log('................................S026................................');

var fn = xiaoming.age; // 先拿到xiaoming的age函数
fn(); // NaN
// 要保证this指向正确,必须用obj.xxx()的形式调用！
console.log('................................S026................................');


console.log('................................S027................................');
// 这是一个巨大的设计错误,ECMA决定在strict模式下让函数的this指向undefined

'use strict';

var xiaoming = {
    name: '小明',
    birth: 1990,
    age: function () {
        var y = new Date().getFullYear();
        return y - this.birth;
    }
};

var fn = xiaoming.age;
console.log(fn()); // Uncaught TypeError: Cannot read property 'birth' of undefined
console.log('................................S027................................');


console.log('................................S028................................');
'use strict';

var xiaoming = {
    name: '小明',
    birth: 1990,
    age: function () {
        var that = this; // 在方法内部一开始就捕获this
        function getAgeFromBirth() {
            var y = new Date().getFullYear();
            return y - that.birth; // 用that而不是this
        }
        return getAgeFromBirth();
    }
};

console.log(xiaoming.age()); // 29
// 用var that = this;,可以放心地在方法内部定义其他函数,而不是把所有语句都堆到一个方法中。
console.log('................................S028................................');


console.log('................................S029................................');
// 在一个独立的函数调用中,根据是否是strict模式,this指向undefined或window

function getAge() {
    var y = new Date().getFullYear();
    return y - this.birth;
}

var xiaoming = {
    name: '小明',
    birth: 1990,
    age: getAge
};

xiaoming.age(); // 29
getAge.apply(xiaoming, []); // 29,this指向xiaoming,参数为空
// apply方法指定函数的this指向哪个对象,接收两个参数,第一个参数是需要绑定的this变量,第二个参数是Array,表示函数本身的参数。
console.log('................................S029................................');

// 另一个与apply()类似的方法是call(),唯一区别是：apply()把参数打包成Array再传入；call()把参数按顺序传入。

Math.max.apply(null, [3, 5, 4]); // 5
Math.max.call(null, 3, 5, 4); // 5
// 对普通函数调用,通常把this绑定为null。
console.log('................................S029................................');


console.log('................................S030................................');
// 装饰器
'use strict';

var count = 0;
var oldParseInt = parseInt; // 保存原函数

window.parseInt = function () {
    count += 1;
    return oldParseInt.apply(null, arguments); // 调用原函数
};

// 测试:
parseInt('10');
parseInt('20');
parseInt('30');
console.log('count = ' + count); // count = 3
console.log('................................S030................................');

```

### 第04节(高阶函数)

@import "廖雪峰JavaScript教程020.jpg"

```JavaScript

// 高阶函数(Higher-order function);一个函数接收另一个函数作为参数,这种函数就称为高阶函数。

'use strict';

function add(x, y, f) { // 一个最简单的高阶函数
    return f(x) + f(y);
}

var x = add(-5, 6, Math.abs);
console.log(x); // 11

```

#### 第01条(map/reduce)

@import "廖雪峰JavaScript教程021.jpg"

[Array.prototype.map()文档](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)

```JavaScript

console.log('................................S031................................');
// map()方法定义在JavaScript的Array中,结果返回一个新的Array
'use strict';

function pow(x) {
    return x * x;
}
var arr = [1, 2, 3, 4, 5, 6, 7, 8, 9];
var results = arr.map(pow); // [1, 4, 9, 16, 25, 36, 49, 64, 81]
console.log(results); // [1, 4, 9, 16, 25, 36, 49, 64, 81]


var arr = [1, 2, 3, 4, 5, 6, 7, 8, 9];
arr.map(String); // ['1', '2', '3', '4', '5', '6', '7', '8', '9']
// 把Array所有数字转为字符串
console.log('................................S031................................');


console.log('................................S032................................');
// Array的reduce()把一个函数作用于Array,这个函数必须接收两个参数,reduce()把结果继续和序列的下一个元素做累积计算
[x1, x2, x3, x4].reduce(f) = f(f(f(x1, x2), x3), x4)


var arr = [1, 3, 5, 7, 9];
arr.reduce(function (x, y) {
    return x + y;
}); // 25
console.log('................................S032................................');


console.log('................................S033................................');
// 字符串转换为Number
'use strict';

function string2int(s) {
    let arr = s.split("");
    arr = arr.map(function (x) {
        return x * 1;
    });
    arr = arr.reduce(function (x, y) {
        return x * 10 + y
    });
    return arr;
}

// 测试:
if (string2int('0') === 0 && string2int('12345') === 12345 && string2int('12300') === 12300) {
    if (string2int.toString().indexOf('parseInt') !== -1) {
        console.log('请勿使用parseInt()!');
    } else if (string2int.toString().indexOf('Number') !== -1) {
        console.log('请勿使用Number()!');
    } else {
        console.log('测试通过!');
    }
} else {
    console.log('测试失败!');
}
console.log('................................S033................................');


console.log('................................S034................................');
// 首字母大写
'use strict';

function normalize(arr) {
    let a;
    return arr.map(function (x) {
        a = x.toLowerCase();
        return a.substring(0, 1).toUpperCase() + a.substring(1);
    });
}

// 测试:
if (normalize(['adam', 'LISA', 'barT']).toString() === ['Adam', 'Lisa', 'Bart'].toString()) {
    console.log('测试通过!');
} else {
    console.log('测试失败!');
}
console.log('................................S034................................');


console.log('................................S035................................');
// 字符串变成整数
'use strict';

var arr = ['1', '2', '3'];
var r;
r = arr.map(Number);
console.log(r);
console.log('................................S035................................');

```

#### 第02条(filter)

@import "廖雪峰JavaScript教程022.jpg"

```JavaScript

console.log('................................S036................................');
// Array的filter()把传入的函数依次作用于每个元素,然后根据返回值是true还是false决定保留还是丢弃该元素。

// 过滤偶数
var arr = [1, 2, 4, 5, 6, 9, 10, 15];
var r = arr.filter(function (x) {
    return x % 2 !== 0;
});
r; // [1, 5, 9, 15]
console.log('................................S036................................');

// 过滤空字符串
var arr = ['A', '', 'B', null, undefined, 'C', '  '];
var r = arr.filter(function (s) {
    return s && s.trim(); // 注意：IE9以下的版本没有trim()方法
});
r; // ['A', 'B', 'C']
console.log('................................S036................................');


console.log('................................S037................................');
var arr = ['A', 'B', 'C'];
var r = arr.filter(function (element, index, self) { // 回调函数
    console.log(element); // 依次打印'A', 'B', 'C'
    console.log(index); // 依次打印0, 1, 2
    console.log(self); // self就是变量arr
    return true;
});
console.log('................................S037................................');

// 去除Array的重复元素
'use strict';

var
    r,
    arr = ['apple', 'strawberry', 'banana', 'pear', 'apple', 'orange', 'orange', 'strawberry'];
r = arr.filter(function (element, index, self) {
    return self.indexOf(element) === index; // indexOf总是返回第一个元素的位置
});
console.log(r.toString()); // apple,strawberry,banana,pear,orange
console.log('................................S037................................');


console.log('................................S038................................');
// 用filter()筛选出素数
'use strict';

function get_primes(arr) {
    return arr.filter(function (x) {
        if (typeof x !== 'number') {
            return false;
        }
        if (x === 0 || x === 1) {
            return false;
        }
        for (let i = 2; i < x; i++) {
            if (x % i === 0) {
                return false;
            }
        }
        return true;
    });
}

// 测试:
var
    x,
    r,
    arr = [];
for (x = 1; x < 100; x++) {
    arr.push(x);
}
r = get_primes(arr);
if (r.toString() === [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97].toString()) {
    console.log('测试通过!');
} else {
    console.log('测试失败: ' + r.toString());
}
console.log('................................S038................................');

```

#### 第03条(sort)

@import "廖雪峰JavaScript教程023.jpg"

```JavaScript

// Array的sort()方法用于排序;通常规定,对于两个元素x和y,如果x < y,返回-1,x == y,返回0,x > y,返回1

['Google', 'Apple', 'Microsoft'].sort(); // ['Apple', 'Google', 'Microsoft']
['Google', 'apple', 'Microsoft'].sort(); // ['Google', 'Microsoft", 'apple']
[10, 20, 1, 2].sort(); // [1, 10, 2, 20]
// sort()方法默认把所有元素先转换为String再排序

console.log('................................S039................................');
'use strict';

var arr = [10, 20, 1, 2];
arr.sort(function (x, y) {
    if (x < y) {
        return -1;
    }
    if (x > y) {
        return 1;
    }
    return 0;
});
console.log(arr); // [1, 2, 10, 20]
console.log('................................S039................................');

// 忽略大小写排序
var arr = ['Google', 'apple', 'Microsoft'];
arr.sort(function (s1, s2) {
    x1 = s1.toUpperCase();
    x2 = s2.toUpperCase();
    if (x1 < x2) {
        return -1;
    }
    if (x1 > x2) {
        return 1;
    }
    return 0;
}); // ['apple', 'Google', 'Microsoft']
console.log('................................S039................................');


// sort()方法会直接对Array进行修改,它返回的结果仍是当前Array

var a1 = ['B', 'A', 'C'];
var a2 = a1.sort();
var a3 = ['A', 'B', 'C'];
console.log(a1); // ['A', 'B', 'C']
console.log(a2); // ['A', 'B', 'C']
console.log(a1 === a2); // true,a1和a2是同一对象
console.log(a3 === a2); // false

```

### 第05节(闭包)

@import "廖雪峰JavaScript教g"

```JavaScript


































































































