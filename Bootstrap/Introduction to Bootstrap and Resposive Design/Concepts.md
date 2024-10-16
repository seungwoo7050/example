# Concepts about This Project

This doc is written in Korean for my convenience.

## 1. 프론트엔드의 기본적인 구성 요소
프론트엔드의 핵심은 웹페이지를 구성하고 사용자가 볼 수 있게 만드는 기술들이며, 이런 작업은 주로 **HTML, CSS, JavaScript**라는 세 가지 주요 언어를 통해 이루어진다.

### HTML (Hyper Text Markup Language)
웹페이지의 구조와 내용을 정의하는 언어다(제목, 본문, 텍스트, 이미지, 링크 등).
```html
<h1>안녕하세요!</h1>
<p>이것은 HTML로 만든 웹페이지입니다.</p>
```

### CSS (Cascading Style Sheets)
HTML 요소의 스타일(색상, 크기, 배치 등)을 정의하는 언어로써 글자/배경 색상, 글꼴 크기 등을 조정한다.
```html
<style>
    h1 {
        color: blue;
    }
</style>
```

### JavaScript
웹페이지의 동적인 기능을 추가하는 스크립트 언어다(예: 버튼 클릭시 동작, 데이터 유효성 검사, 애니메이션 등).
```html
<script>
    function sayHello() {
        alert("안녕하세요!");
    }
</script>
<button onclick="sayHello()">클릭하세요</button >
```

### 브라우저의 HTML 파일 처리 방법

1. **HTML**을 브라우저에 작성하면 브라우저는 HTML 문법을 읽고 페이지의 구조를 렌더링한다.

2. **CSS**를 사용하여 HTML 요소의 스타일을 정의하면 브라우저는 이 스타일을 적용하여 페이지를 꾸민다.

3. **JavaScript**는 브라우저 내에서 실행되어 페이지에 동적인 동작을 추가한다.

### 프론트엔드 프레임워크
프론트엔드 프레임워크(예: **React**, **Vue.js**, **Angular**)는 웹 애플리케이션을 효율적으로 개발하기 위해 미리 정의된 구조, 규칙, 컴포넌트 등을 제공하는 **라이브러리** 또는 **도구 모음**이다.

이를 사용하는 방법은 두 가지가 있는데 

#### 서버에 내장:
라이브러리 파일을 직접 **로컬 서버**에 다운로드하여 사용하는 방법, 이를 통해 애플리케이션이 필요한 모든 라이브러리 파일을 자체 서버에서 불러와 로드할 수 있다.
```html
<script src="path/to/react.js"></script>
```

#### CDN을 통해 동적으로 불러오기:
라이브러리 파일을 **CDN**에서 직접 블러오는 방법이다. CDN을 사용하면 라이브러리를 서버에 직접 다운로드하지 않고, 전 세계에 분산된 CDN 서버에서 빠르게 가져와 사용할 수 있다.
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/react/18.0.0/umd/react.production.min.js"></script>
```

**CDN**은 더 빠르게 웹 페이지를 로드하는 데 유리하다. 반면 **서버에 내장**하는 경우 외부 네트워크에 의존하지 않고 안정적인 파일을 제공할 수 있다.

---

## 2. 기본 HTML 뼈대

기본 HTML 뼈대는 대부분의 웹페이지가 시작할 때 사용하는 기본적인 구조다.
일반적으로 개발자들이 매번 입력하기보다는 이를 복사하여 사용하는 경우가 많다.
이 구조는 웹페이지가 올바르게 표시되고, 브라우저가 HTML 문서를 적절하게 처리할 수 있도록 해준다.
기본 HTML 뼈대는 다음과 같은 요소들로 구성된다:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Document</title>
</head>
<body>
  
</body>
</html>
```

- `<!DOCTYPE html>`: HTML5 문서임을 선언하는 태그. 이를 통해 브라우저는 HTML5 규격에 따라 페이지를 렌더링한다.

- `<html lang="en">`: HTML 문서의 시작을 알리고, 언어 설정을 통해 페이지 언어를 지정한다.

- `<head>`:문서의 메타데이터를 포함하는 부분으로, 스타일시트, 외부 파일 링크, 스크립트, 제목 등이 들어간다.

- `<meta charset="UTF-8">`:문자 인코딩을 UTF-8로 지정하여 다양한 언어를 표현할 수 있게 한다.

- `<meta name="viewport" content="width=device-width, initial-scale-1.0">`: 모바일 장치에서 웹페이지가 적절하게 스케일되도록 설정한다.

- `<title>`: 웹페이지의 제목을 지정하며, 브라우저 탭에 표시된다.

- `<body>`: 실제 화면에 표시되는 콘텐츠가 들어가는 부분이다.

*`skeleton.html` 파일에서 좀 더 자세하게 공부할 수 있다.*

---

## 3. CDN (Content Delivery Network)

**CDN**은 콘텐츠(파일 스크립트, 이미지 등)을 사용자의 지리적 위치에 따라 분산 서버 시스템을 통해 제공하는 기술이다. 서버와 사용자 간의 거리를 줄여 페이지 로딩 시간을 줄이고 성능을 향상시키는 것이 목적이다.

#### Bootstrap에서 CDN을 사용하는 이유:
 Bootstrap을 CDN을 통해 포함하면 전 세계에 분산된 서버에서 Bootstrap 파일을 로드하게 된다. 이는 웹사이트가 Bootstrap을 자신의 서버에서 불러오는 대신, 사용자와 가까운 CDN 서버에서 로드할 수 있게 해줘 웹사이트의 속도가 빨라진다.

#### CDN 사용의 장점:
- **속도**: 가까운 서버에서 파일을 제공하므로 콘텐츠가 빠르게 전달된다.

- **효율성**: 서버에 Bootstrap 파일을 저장할 필요가 없다.

- **캐싱**: 사용자가 이전에 Bootstrap CDN을 사용하여 다른 웹사이트를 방문했다면, Bootstrap 파일이 이미 브라우저에 캐시되어 로딩 속도가 더 빨라질 수 있다.

#### 예시:
아래 명령줄은 브라우저에게 Bootstrap CSS 파일을 CDN에서 로드하도록 지시한다.

```html
<link href="https://cdn.jsdeliver.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
```

---

## 4. 그리드 시스템
**그리드 시스템**은 웹페이지의 레이아웃을 유연하고 반응형으로 만들기 위한 구조이다. Bootstrap의 그리드 시스템은 웹페이지를 12개의 열로 나누고, 화면 크기에 따라 레이아웃이 조정된다(모바일, 태블릿, 데스크탑 등).

### 그리드 시스템 작동 방식:
- 행(row)과 열(col): Bootstrap은 행과 열의 조합을 사용하여 레이아웃을 구성한다.
    - `.row`: 열들을 그룹화 하는 행을 생성한다. 모든 열은 반드시 행 안에 있어야 한다.

    - `.col`: 각 열의 너비를 정의하는데, 12개의 열 중 몇 개를 차지할지 결정한다.

### 반응형 브레이크 포인트:
Bootstrap의 그리드 시스템은 화면 크기에 따라 열의 크기가 조정된다. 다른 장치 크기에 맞춰 열이 얼마나 공간을 차지할지 정의할 수 있다.

- `.col-sm-*`: 작은 화면(예: 휴대폰)에서의 열 크기.

- `.col-md-*`: 중간 화면(예: 태블릿)에서의 열 크기.

- `.col-lg-*`: 큰 화면(예: 데스크탑)에서의 열 크기.

- `.col-xl-*`: 매우 큰 화면에서의 열 크기.

```html
<div class="row">
  <div class="col-md-4">Column 1</div>
  <div class="col-md-4">Column 2</div>
  <div class="col-md-4">Column 3</div>
</div>
```

위 코드는 중간 크기 이상의 화면에서 3개의 열을 가로로 나열하는 예시이다. 작은 화면에서는 열들이 수직으로 쌓인다.

---

## 5. 컨테이너(Container)
Bottstrap에서 **컨테이너**는 레이아웃을 중앙에 정렬하고 콘텐츠를 조직하는 역할을 한다. 컨테이너는 그리드 시스템의 행과 열을 감싸는 요소이다. Bootstrap에는 두 가지 컨테이너 유형이 있다.

- `.container`: 화면 크기에 따라 너비가 고정되며, 큰 화면에서는 최대 너비를 가진다.

- `.container-fluid`: 전체 화면 너비를 차지하며, 화면 크기와 상관없이 항상 100% 너비를 유지한다.

### 컨테이너 사용 목적:
컨테이너는 페이지의 구조를 제공하여 콘텐츠를 중앙에 정렬하고, 좌우에 여백을 추가한다. 또한, 그리드 레이아웃이 다른 화면 크기에서도 적절하게 동작하도록 돕는다.

#### 예시:
컨테이너와 그 안에 두 개의 열을 추가한 예시.
```html
<div class="container">
  <h1>Welcome to Bootstrap</h1>
  <div class="row">
    <div class="col-md-6">Column 1</div>
    <div class="col-md-6">Column 2</div>
  </div>
</div>
```
컨테이너느 콘텐츠를 중앙에 배치하고, 반응형 여백을 추가한다.

---

## 6. Bootstrap 컴포넌트(Component)
**Bootstrap 컴포넌트**는 미리 설계된 UI 요소로, 웹페이지에 빠르게 추가할 수 있는 스타일과 기능을 제공한다. Bootstrap은 버튼, 네비게이션 바, 폼, 알림창, 모달 등 다양한 컴포넌트를 제공한다.

#### Bootstrap 컴포넌트 사용 목적:
- 시간을 절약하며, 일관성 있고 전문적인 디자인 요소를 쉽게 추가할 수 있다.

- 모든 장치에서 반응형으로 동작하며, 다양한 화면 크기에 맞춰 조정된다.

- 컴포넌트는 기본적으로 JavaScript 기능이 내장되어 있어 동적인 동작을 구현할 수 있다(예: 모달, 캐러셀 등).

### 인기 있는 Bootstrap 컴포넌트 예시:
* **버튼**: 사용자가 상호작용할 수 있는 스타일링된 버튼.
```html
<button class="btn btn-primary">Click Me</button>
```

* **네비게이션 바**: 반응형 네비게이션 메뉴.
```html
<nav class="navbar navbar-expand-lg navbar-light bg-light">...</nav>
```

* **폼**: 입력 폼을 미리 스타일링하여 쉽게 만들 수 있다.
```html
<form>...</form>
```

* **알림창**: 경고나 성공 메시지를 나타내는 스타일링된 박스.
```html
<div class="alert alert-success">Success!</div>
```

* **모달**: 팝업 창으로 사용자 상호작용을 위한 창.
```html
<div class="modal" id="myModal">...</div>
```