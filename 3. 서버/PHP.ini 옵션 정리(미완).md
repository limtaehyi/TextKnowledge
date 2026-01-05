## 1. PHP  
<br>

&nbsp;php.ini
- 이 파일은 php의 주요 설정 파일로 php의 동작 제어 옵션들이 포함되어 있어 서버에서 php 스크립트를 어떻게 동작 시킬지를 결정함.
- 세미콜론으로 주석을 달 수 있고 여러 옵션들이 주석 처리 되어 있다.
- quick reference는 대략적으로 옵션을 설정 하며 있어도 되고 없어도 되는 부분이다.
- 이 파일은 php.ini의 설명 주석을 모두 제거한 상태이고 정보보안기사를 위해 정리해 둔 파일이다. 
- 이 파일에서 나의 개인적인 주석은 >을 사용할 것이고 그에 해당하는 옵션은 바로 아랫줄이다.

```
;;;;;;;;;;;;;;;;;;;
; Quick Reference ;
;;;;;;;;;;;;;;;;;;;

; display_errors
;   Default Value: On
;   Development Value: On
;   Production Value: Off

; display_startup_errors
;   Default Value: On
;   Development Value: On
;   Production Value: Off

; error_reporting
;   Default Value: E_ALL
;   Development Value: E_ALL
;   Production Value: E_ALL & ~E_DEPRECATED & ~E_STRICT

; log_errors
;   Default Value: Off
;   Development Value: On
;   Production Value: On

; max_input_time
;   Default Value: -1 (Unlimited)
;   Development Value: 60 (60 seconds)
;   Production Value: 60 (60 seconds)

; output_buffering
;   Default Value: Off
;   Development Value: 4096
;   Production Value: 4096

; register_argc_argv
;   Default Value: On
;   Development Value: Off
;   Production Value: Off

; request_order
;   Default Value: None
;   Development Value: "GP"
;   Production Value: "GP"

; session.gc_divisor
;   Default Value: 100
;   Development Value: 1000
;   Production Value: 1000

; session.sid_bits_per_character
;   Default Value: 4
;   Development Value: 5
;   Production Value: 5

; short_open_tag
;   Default Value: On
;   Development Value: Off
;   Production Value: Off

; variables_order
;   Default Value: "EGPCS"
;   Development Value: "GPCS"
;   Production Value: "GPCS"

; zend.exception_ignore_args
;   Default Value: Off
;   Development Value: Off
;   Production Value: On

; zend.exception_string_param_max_len
;   Default Value: 15
;   Development Value: 15
;   Production Value: 0

;;;;;;;;;;;;;;;;;;;;
; php.ini Options  ;
;;;;;;;;;;;;;;;;;;;;

;user_ini.filename = ".user.ini"
;user_ini.filename =
;user_ini.cache_ttl = 300

;;;;;;;;;;;;;;;;;;;;
; Language Options ;
;;;;;;;;;;;;;;;;;;;;

 > apache에서 php 스크립트 언어 엔진 적용 여부
engine=On

 > php에서 사용하는 <?php 의 줄임말인 <? 의 사용 여부
short_open_tag=Off

 > 부동소수점 유효 자리수
precision=14

output_buffering=4096
;output_handler =
;url_rewriter.tags
;url_rewriter.hosts
zlib.output_compression=Off
;zlib.output_compression_level = -1
;zlib.output_handler =
implicit_flush=Off
unserialize_callback_func=
;unserialize_max_depth = 4096
serialize_precision=-1

 > php가 접근할 수 있는 파일 및 디렉토리 제한
;open_basedir =

disable_functions=
disable_classes=

 > 문법 하이라이트 표시
;highlight.string  = #DD0000
;highlight.comment = #FF9900
;highlight.keyword = #007700
;highlight.default = #0000BB
;highlight.html    = #000000

;ignore_user_abort = On
;realpath_cache_size = 4096k
;realpath_cache_ttl = 120
zend.enable_gc=On
;zend.multibyte = Off
;zend.script_encoding =
zend.exception_ignore_args=Off
zend.exception_string_param_max_len=15

;;;;;;;;;;;;;;;;;
; Miscellaneous ;
;;;;;;;;;;;;;;;;;

 > php 버전 숨기기
expose_php=On

;;;;;;;;;;;;;;;;;;;
; Resource Limits ;
;;;;;;;;;;;;;;;;;;;

 > 스크립트의 최대 실행 시간 (초단위)
max_execution_time=120

max_input_time=60
;max_input_nesting_level = 64
;max_input_vars = 1000
;max_multipart_body_parts = 1500

 > php 메모리 제한 용량
memory_limit=512M

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Error handling and logging ;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

error_reporting=E_ALL & ~E_DEPRECATED & ~E_STRICT

 > php 에러 출력 여부
display_errors=On

 > php 스크립트 시작단계에서 발생하는 에러 출력 여부
display_startup_errors=On

 > php 실행중 발생하는 오류 메세지를 서버의 오류 로그 파일에 기록 여부
log_errors=On

 > 동일 파일의 동일 라인에 반복하는 오류 메세지 기록 무시 여부, 밑에는 다른 파일이나 다른 라인에서 발생하는 오류 처럼 광범위하게 적용 여부
ignore_repeated_errors=Off
ignore_repeated_source=Off

 > 메모리 누수 감지를 보고 할지 여부
report_memleaks=On

;report_zend_debug = 0
;xmlrpc_errors = 0
;xmlrpc_error_number = 0
;html_errors = On

 > 오류 메세지에 포함된 섦여서 링크의 기본 경로
;docref_root = "/phpmanual/"

 > 설명서 파일의 확장자 지정
;docref_ext = .html

 > 오류 출력 특정 문자열 앞에 출력, 특정 문자열 뒤에 출력 
;error_prepend_string = "<span style='color: #ff0000'>"
;error_append_string = "</span>"

 > 오류 로그를 기록할 파일의 경로, 이름 지정
;error_log = php_errors.log
;error_log = syslog

 > syslog에 보낼 식별자, 메세지 종류, 필터링 방식
;syslog.ident = php
;syslog.facility = user
;syslog.filter = ascii

;windows.show_crt_warning

;;;;;;;;;;;;;;;;;
; Data Handling ;
;;;;;;;;;;;;;;;;;

 > URL에서 인자 구분할 문자열 지정
;arg_separator.output = "&amp;"

 > URL에서 파싱하여 변수로 변환할때 사용할 인자 구분, 예를 들어 a=1;b=2 또는 a=1&b=2
;arg_separator.input = ";&"

 > 슈퍼 글로벌 변수가 채워지는 순서 설정 get post cookie server
variables_order="GPCS"
request_order="GP"

register_argc_argv=Off
auto_globals_jit=On
;enable_post_data_reading = Off

 > POST 메세지 최대 크기
post_max_size=40M

 > PHP 스크립트 실행 전후 포함될 파일 지정
auto_prepend_file=
auto_append_file=

 > Content-Type 헤더가 없을 경우 기본적으로 전송되는 MIME 타입 지정
default_mimetype="text/html"

 > PHP가 기본적으로 사용될 문자 인코딩 설정
default_charset="UTF-8"

;internal_encoding =
;input_encoding =
;output_encoding =

;;;;;;;;;;;;;;;;;;;;;;;;;
; Paths and Directories ;
;;;;;;;;;;;;;;;;;;;;;;;;;

 > include, require, fopen등 함수가 파일을 찾을때 탐색하는 디렉토리 지정
include_path=C:\xampp\php\PEAR
;include_path = ".;c:\php\includes"

 > document root 디렉토리 지정, $_SERVER['DOCUMENT_ROOT']의 변수
doc_root=

 > 사용자의 홈 디렉토리 내 PHP 스크립트가 실행될 수 있는 디렉토리
user_dir=

 > PHP가 동적으로 로드할 확장 모듈
extension_dir="C:\xampp\php\ext"

 > 임시 디렉토리 파일
;sys_temp_dir = "/tmp"

 > dl 함수를 사용해서 런타임에 php 확장 모듈을 동적으로 로드하는 기능 활성화 여부
enable_dl=Off

 > php를 cgi로 사용할 때 보안을 위해 리디렉션 강제 여부
;cgi.force_redirect = 1

;cgi.nph = 1
;cgi.redirect_status_env =
;cgi.fix_pathinfo=1
;cgi.discard_path=1

 > fastcgi 환경에서 IIS 같은 웹서버에서 클라이언트의 권한으로 php 스크립트 실행
;fastcgi.impersonate = 1

;fastcgi.logging = 0

 > http 응답 코드를 보낼때 RFC2616 표준을 따르는 헤더를 사용할지 여부
;cgi.rfc2616_headers = 0
;cgi.check_shebang_line=1

;;;;;;;;;;;;;;;;
; File Uploads ;
;;;;;;;;;;;;;;;;

 > php가 http의 post 매서드를 통해 파일 업로드 처리 여부, 업로드 파일 위치, 파일 최대 사이즈, 동시에 업로드 할 수 있는 최대 파일 개수
file_uploads=On
upload_tmp_dir="C:\xampp\tmp"
upload_max_filesize=40M
max_file_uploads=20

;;;;;;;;;;;;;;;;;;
; Fopen wrappers ;
;;;;;;;;;;;;;;;;;;

 > fopen, file_get_contents 등과 같은 파일 시스템 함수가 일반 파일 경로 뿐만이 아닌 원격 파일을 열 수 있는지 허용 여부
allow_url_fopen=On

 > allow_url_fopen이 on일 경우 include, require 함수를 사용하여 원격 서버에 있는 파일을 스크립트에 포함 할 수 있는지 허용 여부
allow_url_include=Off

 > php가 외부 서버에 http 요청 시 from: 헤더에 포함시킬 이메일 주소 설정
;from="john@doe.com"

 > php가 외부 서버에 http 요청 시 user-agnet 헤더에 포함시킬 문자열 설정
;user_agent="PHP"

 > 소켓 기반 함수를 사용할 때 네트워크 작업의 기본 타임아웃의 사간을 초단위로 설정
default_socket_timeout=60

 > php가 csv 파일등에 줄 바꿈 문자를 자동으로 감지할지 여부 설정
;auto_detect_line_endings = Off

;;;;;;;;;;;;;;;;;;;;;;
; Dynamic Extensions ;
;;;;;;;;;;;;;;;;;;;;;;

extension=bz2
;extension=ldap
extension=curl
;extension=ffi
;extension=ftp
extension=fileinfo
;extension=gd
extension=gettext
;extension=gmp
;extension=intl
;extension=imap
extension=mbstring
extension=exif      ; Must be after mbstring as it depends on it
extension=mysqli
;extension=oci8_12c  ; Use with Oracle Database 12c Instant Client
;extension=oci8_19  ; Use with Oracle Database 19 Instant Client
;extension=odbc
;extension=openssl
;extension=pdo_firebird
extension=pdo_mysql
;extension=pdo_oci
;extension=pdo_odbc
;extension=pdo_pgsql
extension=pdo_sqlite
;extension=pgsql
;extension=shmop
;extension=snmp
;extension=soap
;extension=sockets
;extension=sodium
;extension=sqlite3
;extension=tidy
;extension=xsl
;extension=zip
;zend_extension=opcache

;;;;;;;;;;;;;;;;;;;
; Module Settings ;
;;;;;;;;;;;;;;;;;;;

 > asp 스타일의 짧은 태그인 <% ~ %>, <%= ~ %>를 인식하고 php로 처리할건지 여부
asp_tags=Off

 > php 실행 시작시 발생하는 오류 출력 여부
display_startup_errors=On

 > php 실행중 발생한 가장 최근의 오류 메세지를 $php_errormsg 라는 전역변수에 저장 할지 여부
track_errors=Off

y2k_compliance=On
allow_call_time_pass_reference=Off

 > php 5.4 부터 완전히 제거된 옵션들
safe_mode=Off
safe_mode_gid=Off
safe_mode_allowed_env_vars=PHP_
safe_mode_protected_env_vars=LD_LIBRARY_PATH

 > 에러 메세지를 기록할 파일 경로
error_log="C:\xampp\php\logs\php_error_log"

 > php 5.4 부터 완전히 제거된 옵션들
register_globals=Off
register_long_arrays=Off
magic_quotes_gpc=Off
magic_quotes_runtime=Off
magic_quotes_sybase=Off

extension=php_openssl.dll
extension=php_ftp.dll

[CLI Server]
cli_server.color=On

[Date]

 > php에서 날짜 및 시간 함수에 적용되는 기본 시간대 설정
;date.timezone =

 > php에서 지구의 기본 위도, 경도, 일출, 일몰을 설정하며 date_sunrise, date_sunset 함수를 위한 옵션들이다.
;date.default_latitude = 31.7667
;date.default_longitude = 35.2333
;date.sunrise_zenith = 90.833333
;date.sunset_zenith = 90.833333

[filter]
;filter.default = unsafe_raw
;filter.default_flags =

[iconv]
;iconv.input_encoding =
;iconv.internal_encoding =
;iconv.output_encoding =

[imap]
;imap.enable_insecure_rsh=0

[intl]
;intl.default_locale =
;intl.error_level = E_WARNING
;intl.use_exceptions = 0

[sqlite3]

 > sqlite3에는 로드 가능한 확장이 가능한데, 확장 모듈을 찾을 디렉토리 경로 지정
;sqlite3.extension_dir =

 > sqlite3 데이터베이스 연결에 대한 방어 지정
;sqlite3.defensive = 1

[Pcre]
;pcre.backtrack_limit=100000
;pcre.recursion_limit=100000
;pcre.jit=1

[Pdo]
pdo_mysql.default_socket="MySQL"
;pdo_odbc.connection_pooling=strict

[Pdo_mysql]
pdo_mysql.default_socket=

[Phar]
;phar.readonly = On
;phar.require_hash = On
;phar.cache_list =

[mail function]

 > php의 mail 함수가 이메일을 보낼때 사용할 서버의 호스트이름, 포트, 기본 이메일 주소, sendmail 프로그램의 경로 지정
SMTP=localhost
smtp_port=25
;sendmail_from = me@example.com  
;sendmail_path =

 > mail 함수에 추가적으로 전달될 매게 변수
;mail.force_extra_parameters =

 > mail 함수가 이메일 헤더에 X-PHP-Origination-Script 와 같은 추가적인 헤더를 자동으로 추가할지 여부
mail.add_x_header=Off

 > 이메일 메세지에서 줄바꿈 문자로 CRLF가 혼합 사용될 것을 허용할지 여부
mail.mixed_lf_and_crlf=Off

 > mail 함수를 통해 발송되는 모든 이메일 관련 정보 기록 로그 파일 경로
;mail.log =
;mail.log = syslog

[ODBC]

 > 초기 db 연결 관련 설정
;odbc.default_db    =  Not yet implemented
;odbc.default_user  =  Not yet implemented
;odbc.default_pw    =  Not yet implemented
;odbc.default_cursortype

 > ODBC 데이터베이스에 대한 지속적인 연결 허용 여부
odbc.allow_persistent=On

 > ODBC 데이터베이스에 지속적인 연결을 재사용 하기 전에 해당 연결이 유효한지 확인할지 여부
odbc.check_persistent=On

 > 프로세스당 허용되는 최대 지속 연결 수, -1은 무제한
odbc.max_persistent=-1

 > 프로세스당 허용되는 모든 연결 최대 개수 설정
odbc.max_links=-1

odbc.defaultlrl=4096
odbc.defaultbinmode=1

[MySQLi]
mysqli.max_persistent=-1
;mysqli.allow_local_infile = On
;mysqli.local_infile_directory =
mysqli.allow_persistent=On
mysqli.max_links=-1
mysqli.default_port=3306
mysqli.default_socket=
mysqli.default_host=
mysqli.default_user=
mysqli.default_pw=
;mysqli.rollback_on_cached_plink = Off

[mysqlnd]
mysqlnd.collect_statistics=On
mysqlnd.collect_memory_statistics=On
;mysqlnd.debug =
;mysqlnd.log_mask = 0
;mysqlnd.mempool_default_size = 16000
;mysqlnd.net_cmd_buffer_size = 2048
;mysqlnd.net_read_buffer_size = 32768
;mysqlnd.net_read_timeout = 31536000
;mysqlnd.sha256_server_public_key =

[OCI8]
;oci8.privileged_connect = Off
;oci8.max_persistent = -1
;oci8.persistent_timeout = -1
;oci8.ping_interval = 60
;oci8.connection_class =
;oci8.events = Off
;oci8.statement_cache_size = 20
;oci8.default_prefetch = 100
;oci8.prefetch_lob_size = 0
;oci8.old_oci_close_semantics = Off

[PostgreSQL]
pgsql.allow_persistent=On
pgsql.auto_reset_persistent=Off
pgsql.max_persistent=-1
pgsql.max_links=-1
pgsql.ignore_notice=0
pgsql.log_notice=0

[bcmath]
bcmath.scale=0

[browscap]
browscap="C:\xampp\php\extras\browscap.ini"

[Session]
session.save_handler=files
session.save_path="C:\xampp\tmp"
session.use_strict_mode=0
session.use_cookies=1
;session.cookie_secure =
session.use_only_cookies=1
session.name=PHPSESSID
session.auto_start=0
session.cookie_lifetime=0
session.cookie_path=/
session.cookie_domain=
session.cookie_httponly=
session.cookie_samesite=
session.serialize_handler=php
session.gc_probability=1
session.gc_divisor=1000
session.gc_maxlifetime=1440
session.referer_check=
session.cache_limiter=nocache
session.cache_expire=180
session.use_trans_sid=0
session.sid_length=26
session.trans_sid_tags="a=href,area=href,frame=src,form="
;session.trans_sid_hosts=""
session.sid_bits_per_character=5
;session.upload_progress.enabled = On
;session.upload_progress.cleanup = On
;session.upload_progress.prefix = "upload_progress_"
;session.upload_progress.name = "PHP_SESSION_UPLOAD_PROGRESS"
;session.upload_progress.freq =  "1%"
;session.upload_progress.min_freq = "1"
;session.lazy_write = On

[Assertion]
zend.assertions=1
;assert.active = On
;assert.exception = On
;assert.warning = On
;assert.bail = Off
;assert.callback = 0

[COM]
;com.typelib_file =
;com.allow_dcom = true
;com.autoregister_typelib = true
;com.autoregister_casesensitive = false
;com.autoregister_verbose = true
;com.code_page=
;com.dotnet_version=

[mbstring]
;mbstring.language = Japanese
;mbstring.internal_encoding =
;mbstring.http_input =
;mbstring.http_output =
;mbstring.encoding_translation = Off
;mbstring.detect_order = auto
;mbstring.substitute_character = none
;mbstring.strict_detection = Off
;mbstring.http_output_conv_mimetypes=
;mbstring.regex_stack_limit=100000
;mbstring.regex_retry_limit=1000000

[gd]
;gd.jpeg_ignore_warning = 1

[exif]
;exif.encode_unicode = ISO-8859-15
;exif.decode_unicode_motorola = UCS-2BE
;exif.decode_unicode_intel    = UCS-2LE
;exif.encode_jis =
;exif.decode_jis_motorola = JIS
;exif.decode_jis_intel    = JIS

[Tidy]
;tidy.default_config = /usr/local/lib/php/default.tcfg
tidy.clean_output=Off

[soap]
soap.wsdl_cache_enabled=1
soap.wsdl_cache_dir="/tmp"
soap.wsdl_cache_ttl=86400
soap.wsdl_cache_limit=5

[sysvshm]
;sysvshm.init_mem = 10000

[ldap]
ldap.max_links=-1

[dba]
;dba.default_handler=

[opcache]
;opcache.enable=1
;opcache.enable_cli=0
;opcache.memory_consumption=128
;opcache.interned_strings_buffer=8
;opcache.max_accelerated_files=10000
;opcache.max_wasted_percentage=5
;opcache.use_cwd=1
;opcache.validate_timestamps=1
;opcache.revalidate_freq=2
;opcache.revalidate_path=0
;opcache.save_comments=1
;opcache.record_warnings=0
;opcache.enable_file_override=0
;opcache.optimization_level=0x7FFFBFFF
;opcache.dups_fix=0
;opcache.blacklist_filename=
;opcache.max_file_size=0
;opcache.consistency_checks=0
;opcache.force_restart_timeout=180
;opcache.error_log=
;opcache.log_verbosity_level=1
;opcache.preferred_memory_model=
;opcache.protect_memory=0
;opcache.restrict_api=
;opcache.mmap_base=
;opcache.cache_id=
;opcache.file_cache=
;opcache.file_cache_only=0
;opcache.file_cache_consistency_checks=1
;opcache.file_cache_fallback=1
;opcache.huge_code_pages=0
;opcache.validate_permission=0
;opcache.validate_root=0
;opcache.opt_debug_level=0
;opcache.preload=
;opcache.preload_user=
;opcache.file_update_protection=2
;opcache.lockfile_path=/tmp

[curl]
curl.cainfo="C:\xampp\apache\bin\curl-ca-bundle.crt"

[openssl]
openssl.cafile="C:\xampp\apache\bin\curl-ca-bundle.crt"
;openssl.capath=

[ffi]
;ffi.enable=preload

;ffi.preload=
[Syslog]
define_syslog_variables=Off
[Session]
define_syslog_variables=Off
[Date]
date.timezone=Europe/Berlin
[MySQL]
mysql.allow_local_infile=On
mysql.allow_persistent=On
mysql.cache_size=2000
mysql.max_persistent=-1
mysql.max_link=-1
mysql.default_port=3306
mysql.default_socket="MySQL"
mysql.connect_timeout=3
mysql.trace_mode=Off
[Sybase-CT]
sybct.allow_persistent=On
sybct.max_persistent=-1
sybct.max_links=-1
sybct.min_server_severity=10
sybct.min_client_severity=10
[MSSQL]
mssql.allow_persistent=On
mssql.max_persistent=-1
mssql.max_links=-1
mssql.min_error_severity=10
mssql.min_message_severity=10
mssql.compatability_mode=Off
mssql.secure_connection=Off
```