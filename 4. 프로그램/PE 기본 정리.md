## 1. 가상주소공간  
<br> 

&nbsp;배경
- 물리적인 접근 금지
- 단편화 문제
- 부족한 메모리 문제

<br>
<br>

## 2. 윈도우 프로세스 매핑  
<br>

&nbsp;Mapping Table
- 각각의 프로세스를 가상주소공간을 부여 후 물리메모리에 매핑
- 가상의 주소 공간과 물리 주소 공간의 매핑은 운영체제가 관리
- 프로세스들의 가상주소가 같을 수 있어도 물리주소가 다름
- 프로세스는 물리 메모리의 주소 공간을 알수없고 직접 접근도 불가능
- 물리 메모리에 오랫동안 사용하지 않으면 다시 저장소에 보냄; page out
- 다시 사용하면 물리 메모리에 올림; page in

<br>
<br>

## 3. PE  
<br>

&nbsp;Header 종류
- DOS header
- MS-DOS Stub
- NT headers

<br>

&nbsp;Body 종류
- .text; 컴파일 된 기계어 코드, 바이너리
- .data; 전역변수
- .idata; import 변수, 보통 exe 파일내에 있음, dll이나 api 이름
- .rsrc; 리소스
- CODE
- DATA
- BSS
- certificate table; 인증서

<br>
<br>

## 4. DOS header  
<br>

&nbsp;구조
- 메모리에 실행파일을 올릴때 먼저 로더가 먼저 올라간다.
- 구 윈도우와 호완하기 위해 존재하며 로더가 실행파일의 DOS header를 먼저 읽는다.

<br>
<br>

## 5. NT headers  
<br>

&nbsp;구조
- signature
- image_file_header
- image_optional_header

<br>

&nbsp;Image_optional_header
- Imagebase : 실행 파일이 로드될 가상 주소공간의 주소, 유일하게 절대값인 가상주소로 표현되어 있다. 단 메모리의 직접적인 주소는 아니다. 또한 다른 나머지들은 offset(거리차이)값으로 표현
- addressofentrypoint : 메모리에 로드된 후 가장 먼저 실행될 코드의 위치
- filealignment : 파일 주소 시작 위치, 각각의 세션의 위치 정렬
- sectionalignment : 메모리 상의 각 세션의 정렬 단위
- 섹션 개수, 세션 위치값, 섹션 권한 등

<br>

&nbsp;VA
- 매핑될 메모리 주소

<br>

&nbsp;offset
- 이격

<br>
<br>

## 6. 파일과 프로세스  
<br>

&nbsp;기준
- 실행파일이 파일로 존재할때는 header, section들로 이루어져 있고 붙어있지만 메모리에 매핑될때는 imagebase를 기준으로 sectionalignment들의 페이지의 크기를 기준으로 기본적인 공간들을 나누며 빈공간은 padding영역으로 채운다
- 그 이유는 메모리 보호의 목적이다. 각 section들은 권한이 있는데 e, r, w가 protection이다. section별로 다른 권한 설정 하는 것이 좋다.

<br>
<br>

## 7. section table  
<br>

&nbsp;가상주소와 물리주소
- section header에 있는 pointertorawdata는 파일 시작지점부터 ~떨어진 위치에 첫 섹션 존재
- VA는 메모리에 올라간 파일의 시작위치에서 ~떨어진 위치에 첫 섹션존재
- characteristics은 section들의 권한 표기

<br>
<br>

## 8. import  
<br>

- 로더가 파일을 메모리에 올린후 다른 dll을 import하기 위해 image_import_descriptor가 있고 여기에 dll과 api 주소 값을 저장한다
- 메모리 보호 기법인 aslr 때문에 import할 dll,api주소는 로딩이 된후 직접 찾아서 파일의 iat에 입력하는데 이걸 binding이라 한다.
- 한개의 dll마다 originalfirstthunk, timedatestamp, forwarderchain, name, firstchunk가 세트로 있다. 
- name에는 dll의 이름이 있다.
- firstthunk는 함수의 주소 값이 있다. 즉 iat에 쓴다.

<br>
<br>

## 9. SECTION .idata  
<br>

&nbsp;Directory table
- 사용하는 dll의 이름들이 명시 되어 있다.

<br>

&nbsp;Address table
- 사용하는 dll의 함수들이 명시 되어 있다.

<br>
<br>

## A. tool  
<br>

- x64dbg
- x32dbg
- sysinternals
- stud_pe
- cff explorer