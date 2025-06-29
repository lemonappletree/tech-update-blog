# 🛠️ 2025-06-29 기술 업데이트 요약

## 🔹 Kubernetes - Image Compatibility In Cloud Native Environments
이 블로그 글은 클라우드 네이티브 환경에서 이미지 호환성의 중요성을 다루고 있습니다. 특히 통신, 고성능 및 AI 컴퓨팅과 같은 산업에서는 컨테이너화된 애플리케이션이 특정 운영 체제 구성이나 하드웨어를 필요로 하는 경우가 많습니다. 따라서 특정 커널 버전, 드라이버, 시스템 구성 요소 사용을 요구하는 경우가 흔합니다. 이러한 요구 사항을 해결하기 위해 Kubernetes의 Node Feature Discovery(NFD) 프로젝트가 개발되었습니다. NFD는 클러스터 노드의 하드웨어 및 시스템 기능을 자동으로 감지하고 보고하여 특정 시스템 요구 사항을 충족하는 노드에 워크로드를 스케줄링할 수 있도록 돕습니다.

컨테이너 이미지 호환성의 필요성과 다중 클라우드 및 하이브리드 클라우드 환경에서의 과제도 언급됩니다. 다양한 클라우드 제공업체가 각기 다른 운영 체제를 제공하기 때문에 호환성 문제가 발생할 수 있습니다. 이를 해결하기 위해 Open Containers Initiative에서 이미지 호환성 메타데이터 표준을 도입하려는 노력이 진행되었습니다. 이는 Kubernetes Node Feature Discovery 프로젝트에 구현되었으며, 사용자가 하드웨어 및 소프트웨어의 기능을 기반으로 컨테이너를 노드와 일치시켜 지능적인 스케줄링과 워크로드 최적화를 가능하게 합니다.

마지막으로, Kubernetes에서 이미지 호환성을 통해 미션 크리티컬한 워크로드가 호스트 OS 요구 사항을 더 효율적으로 정의하고 검증할 수 있게 되었음을 강조하며, 관련 프로젝트에 참여할 것을 권장합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/06/25/image-compatibility-in-cloud-native-environments/)

## 🔹 Spring Boot - Spring Cloud 2023.0.6 (aka Leyton) Has Been Released
Spring Cloud 2023.0.6(Leyton) 버전이 출시되었습니다. 이 버전은 Spring Boot 3.3.13을 기반으로 하며, 다양한 버그가 수정되었습니다. 이번 릴리스는 Spring Cloud 2023.0.x의 마지막 오픈 소스 버전이며, 2025년 7월 1일부터는 상업적 지원만 제공됩니다. 주요 변경 사항으로는 Spring Cloud Gateway의 httpClient connectTimeout 설정 재로드 지원, Spring Cloud Circuitbreaker의 openTimeout 및 resetTimeout 사용자 정의 기능 추가 등이 있습니다. 또한, Spring Cloud Contract의 일부 아티팩트가 Maven Central에서 더 이상 제공되지 않으며, Docker 이미지나 소스에서 직접 빌드하여 사용할 수 있습니다. 이번 업데이트에는 여러 모듈이 포함되어 있으며, 버전과 관련 문제는 각각의 GitHub 릴리스 페이지에서 확인할 수 있습니다. Maven과 Gradle을 사용한 시작 방법도 제공됩니다.
👉 [자세히 보기](https://spring.io/blog/2025/06/27/spring-cloud-2023-0-6-released)

## 🔹 Docker - Building an Easy Private AI Assistant with Goose and Docker Model Runner
이 기술 블로그 글은 Goose와 Docker Model Runner를 사용하여 개인 AI 비서를 구축하는 방법에 대해 설명합니다. Goose는 AI 모델을 활용하여 개발 작업을 자동화하는 혁신적인 CLI 도구입니다. Docker Model Runner는 Docker를 사용하여 로컬에서 AI 모델을 쉽게 배포할 수 있도록 도와줍니다. 이 두 기술을 결합하면 고급 AI 지원 기능을 갖춘 강력한 로컬 환경이 만들어지며, 이는 코딩 및 자동화에 이상적입니다. 로컬에서 AI 기반 개발 작업을 원활하게 실행하고자 하는 사람들에게 적합한 솔루션을 제공합니다.
👉 [자세히 보기](https://www.docker.com/blog/building-an-ai-assistant-with-goose-and-docker-model-runner/)

## 🔹 Java - JEP targeted to JDK 25: 514: Ahead-of-Time Command-Line Ergonomics
JEP 514는 JDK 25를 목표로 하는 기술로, "Ahead-of-Time Command-Line Ergonomics"를 다룹니다. 이 기능은 커맨드 라인 사용의 효율성을 향상시키기 위한 것으로, 자바 개발자들이 더 나은 사용자 경험을 할 수 있도록 돕습니다.
👉 [자세히 보기](https://inside.java/2025/06/26/jep514-target-jdk25/)

## 🔹 Golang - [ On | No ] syntactic support for error handling
이 블로그 글은 Go 언어 팀이 오류 처리를 위한 구문 지원 계획에 대해 설명합니다. Go 팀은 오류 처리의 중요성을 인식하고 있으며, 이를 개선하기 위한 다양한 방법을 검토하고 있습니다. 현재로서는 특정 구문 지원을 추가할 계획은 없지만, 커뮤니티의 피드백을 바탕으로 지속적으로 검토할 것이라고 합니다.
👉 [자세히 보기](https://go.dev/blog/error-syntax)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
블로그 글 요약: Helm 팀이 2025년 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU에 참가합니다. 올해 말 출시 예정인 Helm 4에 대한 논의가 진행될 예정이니, 행사 기간 동안 발표 세션과 Project Pavilion의 Helm 부스를 방문해 대화에 참여해 보세요. 주간 동안의 모든 Helm 관련 활동에 대한 자세한 내용은 본문에서 확인할 수 있습니다.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

