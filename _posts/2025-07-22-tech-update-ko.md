# 🛠️ 2025-07-22 기술 업데이트 요약

## 🔹 Kubernetes - Post-Quantum Cryptography in Kubernetes
이 블로그 글은 양자 컴퓨팅의 발전에 따라 암호화 기술이 큰 변화를 맞이하고 있는 상황을 다루고 있습니다. 현재의 암호화 표준이 양자 컴퓨터에 의해 깨질 가능성이 있기 때문에, 장기적으로 사용되는 시스템에서는 이를 대비해야 합니다. 이러한 이유로 `포스트 양자 암호화`(PQC)가 주목받고 있으며, 특히 Kubernetes 생태계에서의 TLS에 미치는 영향을 설명하고 있습니다.

PQC는 고전 컴퓨터와 양자 컴퓨터 모두에 대해 안전하다고 여겨지는 암호화 알고리즘을 의미합니다. NIST에서 표준화한 `모듈-라티스 키 캡슐화 메커니즘`(ML-KEM)과 같은 알고리즘을 통해 이러한 전환이 이루어지고 있습니다. TLS에서 주요한 암호화 작업인 키 교환과 디지털 서명을 안전하게 유지하는 것이 중요합니다.

현재 Kubernetes는 Go 언어를 사용하고 있으며, Go 1.24 버전부터는 하이브리드 포스트 양자 키 교환 메커니즘인 `X25519MLKEM768`을 기본적으로 지원합니다. 이는 Kubernetes v1.33 버전에서도 기본으로 활성화되어 있으며, 결과적으로 Kubernetes가 양자 안전성을 확보하는 데 중요한 진전을 보이고 있습니다.

이 블로그는 또한 Go 버전의 불일치로 인한 잠재적 문제와 PQC 디지털 서명의 제한 사항을 언급하며, 포스트 양자 서명 구현의 어려움에 대해서도 설명합니다. 이와 관련된 도구체인 지원과 성능 문제도 다루고 있습니다.

결론적으로, Kubernetes가 양자 안전성을 확보하기 위한 여정이 시작되었으며, 포스트 양자 키 교환이 기본적으로 활성화됨에 따라 사용자들은 이미 많은 TLS 연결에서 그 혜택을 보고 있습니다. 하지만 Go 버전 불일치에 따른 문제와 같은 잠재적 함정에 대한 인식이 필요하며, 디지털 서명 및 인증서 계층의 PQC는 아직 초기 단계에 있습니다. Kubernetes의 보안을 장기적으로 보장하기 위해 이러한 발전에 대한 지속적인 관심이 필요합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/07/18/pqc-in-k8s/)

## 🔹 Spring Boot - Spring AMQP 4.0 Milestone 3 Available
Spring AMQP 4.0.0의 세 번째 마일스톤이 발표되었습니다. 이번 업데이트에서는 Jackson 3 지원 추가 및 Jackson 2 구성요소의 사용 중단, JUnit 4 구성요소의 사용 중단, 종료 단계에서 `BlockingQueueConsumer`의 개선이 이루어졌습니다. 또한, 패치 버전 3.2.6도 함께 출시되었습니다. 더 자세한 정보는 릴리스 노트를 참조하시고, 프로젝트 관련 문의는 GitHub 이슈를 통해 연락 바랍니다.
👉 [자세히 보기](https://spring.io/blog/2025/07/21/spring-amqp-4-0-0-m3-available)

## 🔹 Docker - Docker Unveils the Future of Agentic Apps at WeAreDevelopers
Docker는 WeAreDevelopers 행사에서 '에이전트 앱'의 미래를 소개했습니다. 에이전트 앱이란 대규모 언어 모델(LLM)을 사용하여 목표에 기반한 실행 워크플로우를 정의하고, 사용자의 도구, 데이터 및 시스템에 접근하는 애플리케이션을 의미합니다. 이 글에서는 이러한 앱의 정의와 함께, 빌드, 테스트, 배포를 더 쉽게 할 수 있는 방법에 대해 설명합니다. 새로운 요소들이 이 애플리케이션 스택에 추가되었음을 강조합니다.
👉 [자세히 보기](https://www.docker.com/blog/wearedevelopers-docker-unveils-the-future-of-agentic-apps/)

## 🔹 Java - JEP targeted to JDK 25: 518: JFR Cooperative Sampling
블로그 글 요약: JEP 518은 JDK 25를 목표로 하고 있으며, JFR(Cooperative Sampling)을 도입하는 내용을 담고 있습니다. 이는 Java Flight Recorder의 성능을 향상시키기 위한 기능입니다.
👉 [자세히 보기](https://inside.java/2025/07/21/jep518-target-jdk25/)

## 🔹 Golang - The FIPS 140-3 Go Cryptographic Module
Title: FIPS 140-3 Go 암호화 모듈

요약: Go 언어는 이제 내장된 FIPS 140-3 준수 모드를 지원합니다.
👉 [자세히 보기](https://go.dev/blog/fips140)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
제목: Helm @ KubeCon + CloudNativeCon EU '25

요약: Helm 팀이 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU '25에 참가합니다. 올해 말 출시 예정인 Helm 4와 관련하여 토론 세션과 프로젝트 전시관의 Helm 부스에서 유지보수자들과 소통할 수 있는 기회가 마련되어 있습니다. 이번 주 동안 진행될 모든 Helm 관련 활동에 대한 자세한 내용은 아래 링크를 참조하세요.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

