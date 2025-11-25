# 🛠️ 2025-11-25 기술 업데이트 요약

## 🔹 Kubernetes - Ingress NGINX Retirement: What You Need to Know
Ingress NGINX가 2026년 3월에 종료될 예정이라는 발표가 있었습니다. 이후에는 추가 릴리스, 버그 수정, 보안 취약점 업데이트가 제공되지 않으며 GitHub 저장소는 읽기 전용으로 유지됩니다. 기존 Ingress NGINX 배포는 여전히 작동하며 설치 아티팩트도 계속 사용할 수 있습니다. 사용자는 Gateway API나 다른 대안 Ingress 컨트롤러로의 전환을 권장받고 있습니다. Ingress NGINX는 Kubernetes 프로젝트 초기의 인기 있는 컨트롤러였지만, 유지보수 인력 부족과 기술 부채로 인해 종료됩니다. 사용자는 클러스터 관리자로 명령어를 실행해 Ingress NGINX 사용 여부를 확인할 수 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/11/11/ingress-nginx-retirement/)

## 🔹 Spring Boot - Towards Spring Tools 5 - Ready for Boot 4 and Framework 7
이 블로그 글은 Spring Framework 7과 Spring Boot 4의 주요 업데이트에 맞춰 새롭게 출시될 Spring Tools 5에 대해 소개합니다. Spring Tools 5는 새로운 API 버전 관리, 함수형 빈 정의, JSpecify 기반의 널 분석 자동 구성, AOT 리포지토리 지원 등 다양한 기능을 지원합니다. API 버전 관리는 서버 및 클라이언트 측 웹 엔드포인트에서 유용하며, 빈 등록자는 프로그래밍 방식으로 구조화된 빈 정의를 가능하게 합니다. 또한, Spring Data의 AOT 리포지토리는 쿼리 세부 정보를 코드에 직접 표시하여 개발자가 SQL 쿼리 생성을 이해할 수 있도록 돕습니다. JSpecify 주석 기반의 널 분석은 Eclipse와 같은 환경에서 자동으로 구성됩니다. 12월 10일 GA 출시 전, 최신 릴리스 후보를 시도해볼 수 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/11/24/towards-spring-tools-5-part1)

## 🔹 Docker - Security that moves fast: Docker’s response to Shai Hulud 2.0
제목: 빠르게 움직이는 보안: Shai Hulud 2.0에 대한 Docker의 대응

요약: 2025년 11월 21일, 보안 연구자들은 가장 공격적인 npm 공급망 공격 중 하나가 시작되는 것을 감지했습니다. Shai Hulud 2.0 캠페인은 72시간 내에 25,000개 이상의 GitHub 저장소를 침해했으며, Zapier, ENS Domains, PostHog, Postman 등 주요 조직의 패키지를 대상으로 했습니다. 이 악성 소프트웨어는 자체 전파 설계로 인해 큰 피해를 일으켰습니다.
👉 [자세히 보기](https://www.docker.com/blog/security-that-moves-fast-dockers-response-to-shai-hulud-2-0/)

## 🔹 Java - JEP targeted to JDK 26: 525: Structured Concurrency (6th Preview)
블로그 글은 JDK 26에 목표로 하고 있는 JEP 525: Structured Concurrency의 여섯 번째 프리뷰에 대한 내용을 다루고 있습니다. Structured Concurrency는 Java의 동시성 프로그래밍을 더 직관적이고 오류가 적게 만들기 위한 기법입니다. 이 프리뷰에서는 이전 버전에서 개선된 사항과 새로운 기능들이 추가되어 JDK 26에 통합될 예정입니다.
👉 [자세히 보기](https://inside.java/2025/11/24/jep525-target-jdk26/)

## 🔹 Golang - Go’s Sweet 16
제목: Go의 16번째 생일

요약: Go 프로그래밍 언어의 16번째 생일을 축하하는 글입니다. Go 언어의 개발 역사와 주요 발전 사항을 돌아보며 기념하는 내용을 담고 있습니다.
👉 [자세히 보기](https://go.dev/blog/16years)

