# 🛠️ 2025-06-28 기술 업데이트 요약

## 🔹 Kubernetes - Image Compatibility In Cloud Native Environments
이 블로그 글은 클라우드 네이티브 환경에서의 이미지 호환성에 대해 다룹니다. 특정 성능 기준을 충족해야 하는 산업에서는 컨테이너화된 애플리케이션이 특정 운영 체제 설정이나 하드웨어를 필요로 합니다. Open Container Initiative (OCI)가 존재하지만, 호환성 요구 사항을 표현하는 데에는 여전히 어려움이 있습니다. 이를 해결하기 위해 Kubernetes의 Node Feature Discovery (NFD)가 개발되었습니다. NFD는 클러스터 노드의 하드웨어 및 시스템 특징을 자동으로 감지하고 보고하여, 특정 시스템 요구 사항을 만족하는 노드에 워크로드를 스케줄링하는 데 도움을 줍니다. 

호환성 사양의 필요성과 다양한 클라우드 환경에서의 문제를 해결하기 위해, OCI Image Compatibility 작업 그룹에서 호환성 메타데이터의 표준화를 위한 노력이 진행되었습니다. Kubernetes NFD 프로젝트는 이러한 호환성 요구 사항을 이미지 메니페스트에 표현하고, 자동 검증을 지원하는 사양을 구현했습니다. 이를 통해 컨테이너를 스케줄링하기 전에 호환성을 확인할 수 있습니다.

블로그 글은 호환성 사양을 정의하고, 이미지를 OCI 아티팩트로 첨부하여 호환성을 검증하는 방법을 설명합니다. Kubernetes를 통해 호환성을 통합함으로써, 중요한 워크로드가 호스트 운영 체제 요구 사항을 보다 효율적으로 정의하고 검증할 수 있게 되었습니다. 마지막으로, Kubernetes Node Feature Discovery 프로젝트에 참여하여 이미지 호환성 API와 도구의 설계 및 개발에 기여할 수 있다고 안내합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/06/25/image-compatibility-in-cloud-native-environments/)

## 🔹 Spring Boot - Spring Cloud 2023.0.6 (aka Leyton) Has Been Released
Spring Cloud 2023.0.6 릴리스가 발표되었습니다. 이 릴리스는 Spring Boot 3.3.13을 기반으로 하며, 여러 버그 수정 및 개선 사항이 포함되어 있습니다. 2023.0.x 버전의 마지막 오픈 소스 릴리스로, 2025년 7월 1일부터는 상업적 지원만 제공됩니다. 주요 변경 사항으로는 Spring Cloud Gateway의 httpClient connectTimeout 재로드 지원 및 Spring Cloud Circuitbreaker의 openTimeout과 resetTimeout 사용자 정의 기능 추가가 있습니다. 또한, Spring Cloud Contract는 Maven Central에서 실행 가능한 jar 파일의 배포가 중단됨에 따라 spring-cloud-stub-runner-boot 아티팩트가 더 이상 제공되지 않습니다. 사용자는 Docker 이미지나 소스 빌드를 통해 이를 사용할 수 있습니다. 이번 릴리스에 포함된 각 모듈은 업데이트되었으며, 자세한 내용은 GitHub 릴리스 페이지에서 확인할 수 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/06/27/spring-cloud-2023-0-6-released)

## 🔹 Docker - Building an Easy Private AI Assistant with Goose and Docker Model Runner
이 기술 블로그 글은 Goose와 Docker Model Runner를 사용하여 개인 AI 비서를 구축하는 방법에 대해 설명합니다. Goose는 AI 모델을 활용하여 개발 작업을 자동화하는 혁신적인 CLI 도구이며, Docker Model Runner는 AI 모델을 로컬에서 Docker를 통해 쉽게 배포할 수 있도록 도와줍니다. 이 두 기술을 결합하면 고급 AI 지원을 통해 코딩 및 자동화를 위한 강력한 로컬 환경을 만들 수 있습니다. 로컬에서 손쉽게 AI 기반 개발 작업을 실행하려는 사람들에게 적합한 솔루션을 제공합니다.
👉 [자세히 보기](https://www.docker.com/blog/building-an-ai-assistant-with-goose-and-docker-model-runner/)

## 🔹 Java - JEP targeted to JDK 25: 514: Ahead-of-Time Command-Line Ergonomics
블로그 글은 JDK 25를 목표로 하는 JEP 514에 대해 다루고 있습니다. 이 JEP는 "Ahead-of-Time Command-Line Ergonomics"를 주제로 하며, 명령줄에서의 사용자 경험을 향상시키기 위한 기술적 개선 사항을 제안합니다. 자세한 내용은 제공된 링크를 통해 확인할 수 있습니다.
👉 [자세히 보기](https://inside.java/2025/06/26/jep514-target-jdk25/)

## 🔹 Golang - [ On | No ] syntactic support for error handling
이 기술 블로그 글은 Go 언어 팀이 오류 처리에 대한 문법적 지원을 어떻게 계획하고 있는지에 대해 다룹니다. Go 팀은 오류 처리의 효율성을 높이기 위한 여러 가지 접근 방안을 고려하고 있으며, 이 과정에서 언어나 개발자 경험에 미치는 영향을 신중히 검토하고 있습니다. 이 블로그 글은 이러한 계획의 배경과 방향성을 간략히 설명합니다.
👉 [자세히 보기](https://go.dev/blog/error-syntax)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
제목: Helm @ KubeCon + CloudNativeCon EU '25

요약: Helm 팀이 2025년 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU '25에 참여합니다. 올해 말 출시 예정인 Helm 4에 대한 논의가 진행될 예정이며, 세션과 Helm 부스에서 유지 관리자들과의 대화에 참여할 수 있습니다. 행사 기간 동안 진행되는 모든 Helm 관련 활동에 대한 자세한 내용은 아래 링크에서 확인할 수 있습니다.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

