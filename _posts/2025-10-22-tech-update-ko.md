# 🛠️ 2025-10-22 기술 업데이트 요약

## 🔹 Kubernetes - 7 Common Kubernetes Pitfalls (and How I Learned to Avoid Them)
이 기술 블로그 글은 Kubernetes 사용 시 흔히 겪을 수 있는 7가지 함정과 이를 피하는 방법을 설명합니다. Kubernetes는 강력하지만 때로는 좌절감을 줄 수 있는 도구로, 필자는 초기 컨테이너 오케스트레이션 경험 시 많은 실수를 통해 배운 점들을 공유합니다. 주요 함정으로는 리소스 요청 및 제한 설정 누락, 라이브니스 및 레디니스 프로브 과소평가, 컨테이너 로그에만 의존하기, 개발 및 프로덕션 환경을 동일하게 취급하기, 불필요한 리소스 방치, 네트워킹에 너무 빨리 심취하기, 보안 및 RBAC를 소홀히 하는 것 등이 있습니다. 각 항목에서는 문제의 원인과 이를 피하기 위한 구체적인 방법을 제시하며, Kubernetes의 공식 문서 및 커뮤니티 리소스를 활용할 것을 권장합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/10/20/seven-kubernetes-pitfalls-and-how-to-avoid/)

## 🔹 Spring Boot - Multi-Factor Authentication in Spring Security 7
이 블로그 글은 Spring Security 7에서의 다중 요소 인증(MFA) 기능을 소개합니다. MFA는 사용자의 신원을 여러 가지 확인 수단을 통해 인증하는 전략으로, 비밀번호, 앱, 생체 인증 등이 포함됩니다. Spring Security 7은 다양한 MFA 사용 사례를 지원하며, 특정 인증 요소가 필요할 때 이를 요구하는 권한 규칙을 설정할 수 있습니다. 이러한 MFA 기능은 `GrantedAuthority` 개념을 활용하여 구현되며, 사용자 정의 인증 메커니즘도 MFA에 참여할 수 있습니다. 블로그 글은 전역적으로 MFA를 활성화하는 방법, 조건에 맞는 세밀한 MFA 제어 방법, 시간 기반 및 사용자 기반 권한 규칙을 설정하는 방법 등을 설명합니다. 이를 통해 Spring Security 7에서 MFA를 효과적으로 사용할 수 있습니다. 더 알아보기 위해서는 관련 예제 코드와 문서를 참고할 수 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/10/21/multi-factor-authentication-in-spring-security-7)

## 🔹 Docker - Introducing a Richer ”docker model run” Experience
제목: "더욱 풍부해진 'docker model run' 경험 소개"

요약: 개발자들은 명령어 기반의 인터페이스(CLI)에서 많은 시간을 보내며, 강력하고 직관적인 CLI는 작업의 어려움과 즐거움의 차이를 만들어냅니다. 이에 따라, 우리는 Docker Model Runner의 대화형 채팅 경험을 크게 업그레이드한 소식을 전하게 되어 기쁩니다. Docker Model Runner는 AI 워크로드를 로컬에서 실행하는 도구로, 이번 업데이트를 통해 더욱 향상된 사용자 경험을 제공합니다.
👉 [자세히 보기](https://www.docker.com/blog/docker-model-run-prompt/)

## 🔹 Java - Assembling Project Leyden #JVMLS
"Project Leyden 조립"이라는 제목의 기술 블로그 글은 두 해 전 JVMLS에서 John Rose가 프로젝트 Leyden의 프로토타입 노력을 공개한 이후의 발전을 다룹니다. 그동안 Leyden은 JDK 24와 JDK 25에 JEPs를 제공했습니다. 이 초기 빌딩 블록들은 새로운 AOT 기능을 계속 조립하는 기반을 제공합니다. 글에서는 AOTCache가 언제, 어떻게 생성되는지 깊이 있게 다루며, Leyden의 다음 계획과 미래 탐구 영역, 그리고 팀이 그동안 배운 놀라운 점들에 대해서도 논의합니다.
👉 [자세히 보기](https://inside.java/2025/10/21/jvmls-assembling-project-leyden/)

## 🔹 Golang - Flight Recorder in Go 1.25
Go 1.25 버전에서는 새로운 진단 도구로서 '비행 기록' 기능이 도입되었습니다. 이 기능은 프로그램 실행 중 발생하는 다양한 이벤트를 기록하고 분석하는 데 유용합니다. 이를 통해 개발자는 프로그램의 성능 문제를 더 쉽게 식별하고 해결할 수 있습니다.
👉 [자세히 보기](https://go.dev/blog/flight-recorder)

## 🔹 Helm - Helm Turns 10
블로그 글 "Helm Turns 10"은 Helm의 10주년을 기념하는 내용입니다. Helm은 10년 전 Kubernetes 1.1.0이 출시된 직후 해커톤에서 처음 탄생했습니다. 초기 Helm의 첫 커밋은 2015년 10월 19일에 이루어졌으며, 이는 Helm v1의 코드베이스가 저장된 helm-classic Git 저장소에서 확인할 수 있습니다. 이후 Helm은 Deployment Manager와 통합되어 Kubernetes 프로젝트의 일부로 발전했습니다.
👉 [자세히 보기](https://helm.sh/blog/helm-turns-ten/)

