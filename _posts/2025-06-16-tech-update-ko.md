# 🛠️ 2025-06-16 기술 업데이트 요약

## 🔹 Kubernetes - Enhancing Kubernetes Event Management with Custom Aggregation
이 기술 블로그 글은 Kubernetes 이벤트 관리의 개선을 위해 커스텀 이벤트 집계 시스템을 구축하는 방법을 설명합니다. Kubernetes 클러스터에서 발생하는 다양한 이벤트는 클러스터 운영에 중요한 통찰력을 제공하지만, 클러스터가 커짐에 따라 이러한 이벤트를 관리하고 분석하는 것이 점점 더 어려워집니다. 이 글은 엔지니어링 팀이 클러스터의 동작을 더 잘 이해하고 문제를 효과적으로 해결할 수 있도록 돕는 커스텀 이벤트 집계 시스템을 구축하는 방법을 다룹니다.

기본적으로, 이 시스템은 이벤트를 모니터링하고 처리하며, 관련성을 분석하여 저장하는 세 가지 주요 구성 요소로 설계됩니다. 이 글에서 제안하는 시스템은 Kubernetes API와의 호환성을 유지하면서 확장성과 신뢰성을 높이기 위한 모범 사례를 따릅니다. 이 시스템을 통해 이벤트를 조기에 감지하고 문제 해결 시간을 단축할 수 있으며, 시스템의 신뢰성을 높일 수 있습니다. 추가적으로, 머신러닝을 이용한 이상 탐지, 인기 있는 관측 플랫폼과의 통합, 애플리케이션별 커스텀 이벤트 API 개발 등으로 시스템을 확장할 수 있는 가능성도 제시합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/06/10/enhancing-kubernetes-event-management-custom-aggregation/)

## 🔹 Spring Boot - Spring Data 2025.0.1, 2024.1.7, and 2024.0.13 released
이 기술 블로그 글은 Spring Data의 세 가지 서비스 릴리스인 `2025.0.1`, `2024.1.7`, `2024.0.13`의 출시를 발표합니다. 이번 릴리스는 종속성 업데이트, 회귀 수정 및 선택된 개선 사항을 포함하고 있습니다. 특히, `2024.0.13` 릴리스는 오픈 소스 생명 주기의 종료를 맞이하여, 사용자들에게 최신 버전인 `3.4.x`로 업그레이드할 것을 권장하고 있습니다. 또한, 다가오는 Spring Boot 릴리스가 이번 업데이트를 반영할 예정입니다. 각 버전별로 Spring Data의 다양한 모듈에 대한 업데이트 내용과 관련 문서, 변경 로그 링크가 제공됩니다.
👉 [자세히 보기](https://spring.io/blog/2025/06/13/spring-data-2025-0-1-2024-1-7-and-2024-0-13-released)

## 🔹 Docker - How to Build, Run, and Package AI Models Locally with Docker Model Runner
이 블로그 글은 Docker Model Runner를 사용하여 로컬에서 AI 모델을 구축, 실행 및 패키지하는 방법에 대해 설명합니다. 글쓴이는 Senior DevOps Engineer이자 Docker Captain으로서 다양한 분야에서 AI 시스템을 구축한 경험을 바탕으로, 현대 인프라에서 AI의 중요성을 강조합니다. 이 가이드는 개발자 친화적인 경량 도구인 Docker Model Runner를 활용하여 AI 모델을 효과적으로 관리하는 방법을 소개합니다.
👉 [자세히 보기](https://www.docker.com/blog/how-to-build-run-and-package-ai-models-locally-with-docker-model-runner/)

## 🔹 Java - Interconnecting Java and Native Code with the FFM API
이 기술 블로그 글은 Java SE 22에 도입된 Foreign Function & Memory Access API(FFM API)가 Java 애플리케이션과 네이티브 라이브러리 간의 차이를 어떻게 줄였는지에 대해 설명합니다. FFM API는 세 가지 단계로 이를 실현합니다. 첫째, FFM API는 오프 힙 메모리 영역을 메모리 세그먼트로 모델링할 수 있는 풍부한 API를 제공합니다. 둘째, 네이티브 함수를 설명하고 연결할 수 있는 풍부한 API를 제공합니다. 셋째, jextract라는 도구를 사용하여 네이티브 라이브러리에 접근하는 데 필요한 FFM API 아티팩트를 자동으로 생성함으로써 접근을 더욱 간소화할 수 있습니다. 이 프레젠테이션은 기본적인 FFM 원칙과 네이티브 그래픽 라이브러리 및 AI 프레임워크와의 Java 통합을 보여줍니다.
👉 [자세히 보기](https://inside.java/2025/06/14/javaone-ffm/)

## 🔹 Golang - [ On | No ] syntactic support for error handling
이 기술 블로그 글은 Go 팀이 오류 처리 지원에 대한 계획을 논의하는 내용입니다. 블로그에서는 Go 언어의 오류 처리 구문에 대한 지원 방향을 설명하고 있으며, 현재의 오류 처리 방법과 향후 개선 방안에 대한 고민을 다루고 있습니다. 이를 통해 개발자들이 더 효율적으로 오류를 처리할 수 있도록 하는 것이 목표입니다.
👉 [자세히 보기](https://go.dev/blog/error-syntax)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
제목: Helm @ KubeCon + CloudNativeCon EU '25  
요약: Helm 팀이 런던에서 열리는 KubeCon + CloudNativeCon EU '25에 참여합니다. 행사는 4월 1일부터 4일까지 열리며, 올해 말 출시 예정인 Helm 4에 대한 논의가 진행됩니다. 참가자들은 발표 세션과 Project Pavilion의 Helm 부스를 통해 유지보수자들과 대화할 수 있습니다. 주간 동안 진행되는 Helm 관련 활동에 대한 자세한 정보는 링크를 통해 확인할 수 있습니다.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

