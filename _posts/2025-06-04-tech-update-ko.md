# 🛠️ 2025-06-04 기술 업데이트 요약

## 🔹 Kubernetes - Start Sidecar First: How To Avoid Snags
이 블로그 글은 Kubernetes에서 사이드카 컨테이너를 메인 애플리케이션보다 먼저 시작하는 방법을 설명합니다. Kubernetes v1.29.0 릴리스에서 사이드카 컨테이너에 대한 네이티브 지원이 추가되었으며, 이를 통해 사이드카 컨테이너를 `.spec.initContainers` 필드에서 정의할 수 있습니다. 그러나 사이드카 컨테이너가 메인 애플리케이션보다 먼저 시작되도록 보장하는 것은 복잡할 수 있습니다. 이 글은 다양한 프로브와 훅을 사용하여 이 문제를 해결하는 방법을 설명합니다. 주요 방법으로는 `readinessProbe`, `livenessProbe`, `startupProbe`, 그리고 `postStart` 라이프사이클 훅이 있습니다. 이 방법들 각각은 사이드카와 메인 애플리케이션의 시작 및 준비 상태에 영향을 미칩니다. 최적의 방법은 `startupProbe`를 사용하여 사이드카가 준비될 때까지 메인 애플리케이션의 시작을 지연시키는 것입니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/06/03/start-sidecar-first/)

## 🔹 Spring Boot - This Week in Spring - June 3rd, 2025
이번 주 Spring 블로그 요약은 IntelliJ IDEA 프로젝트 리드 Aleksey Stukalov와 함께 Java, Kotlin, Spring 개발자들을 위한 새로운 기능에 대해 논의한 세션 녹화로 시작합니다. 또한, JSpring 컨퍼런스에서 발표할 예정입니다. 주요 소식으로는 Spring Cloud 2022.0.11 및 Spring Cloud 2025.0.0 출시, Spring Cloud Gateway의 여러 버전 릴리스, Spring Modulith의 다양한 버전 출시, Vite Spring Boot 0.9.0 릴리스가 포함됩니다. Jetbrains의 IDE에서 Spring Data AOT 리포지토리 지원 및 JPA 엔티티 리버스 엔지니어링 기능도 기대됩니다. Spring Modulith 지원도 예정되어 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/06/03/this-week-in-spring-june-3rd-2025)

## 🔹 Docker - How to Make an AI Chatbot from Scratch using Docker Model Runner
이 기술 블로그 글은 Docker Model Runner를 사용하여 생성형 AI 챗봇을 처음부터 구축하는 방법을 설명합니다. 글에서는 Prometheus, Grafana, Jaeger와 같은 관측 도구들을 활용하여 완전한 기능을 갖춘 챗봇을 만드는 과정을 다룹니다. AI 기반 애플리케이션을 개발할 때 흔히 겪는 문제들을 소개하고, Docker Model Runner가 이러한 문제를 어떻게 해결하는지 보여줍니다. 그런 다음, 단계별로 챗봇을 구축하는 방법을 안내합니다.
👉 [자세히 보기](https://www.docker.com/blog/how-to-make-ai-chatbot-from-scratch/)

## 🔹 Java - What’s new for JFR in JDK 25
JDK 25는 9월 16일에 출시될 예정이며, JFR(Java Flight Recorder)을 위한 세 가지 새로운 Java Enhancement Proposals(JEPs)와 jdk.jfr API 및 jfr 명령어에 대한 여러 개선 사항을 포함할 예정입니다.
👉 [자세히 보기](https://inside.java/2025/06/03/new-jfr-jdk25/)

## 🔹 Golang - [ On | No ] syntactic support for error handling
블로그 글은 Go 팀이 오류 처리 지원에 대한 계획을 다루고 있습니다. 현재 Go 언어는 구문적 오류 처리 지원이 부족하다는 점을 인정하고 있으며 이를 개선하기 위한 논의가 진행 중입니다. 이 블로그는 이러한 계획과 논의의 방향성을 간략히 설명하고 있습니다.
👉 [자세히 보기](https://go.dev/blog/error-syntax)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
블로그 글 요약: Helm 팀이 2025년 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU에 참여합니다. 이번 행사에서는 올해 말 출시 예정인 Helm 4에 대한 논의가 진행될 예정입니다. 참석자들은 프로젝트 파빌리온 내 Helm 부스와 발표 세션에서 Helm 유지보수자들과 대화를 나눌 수 있습니다. 행사 기간 동안 진행될 모든 Helm 관련 활동에 대한 자세한 정보는 블로그에서 확인할 수 있습니다.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

