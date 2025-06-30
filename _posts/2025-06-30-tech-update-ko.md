# 🛠️ 2025-06-30 기술 업데이트 요약

## 🔹 Kubernetes - Image Compatibility In Cloud Native Environments
이 기술 블로그 글은 클라우드 네이티브 환경에서 이미지 호환성 문제를 다루고 있습니다. 통신, 고성능 컴퓨팅, AI 컴퓨팅과 같은 분야에서는 컨테이너화된 애플리케이션이 특정 운영 체제 설정이나 하드웨어가 필요할 수 있습니다. Open Container Initiative(OCI)가 존재하지만 이러한 호환성 요구 사항을 표현하는 데는 여전히 어려움이 있습니다. 이를 해결하기 위해 Kubernetes의 Node Feature Discovery(NFD)가 사용됩니다. NFD는 클러스터 노드의 하드웨어 및 시스템 기능을 자동으로 감지하고 보고하여 특정 시스템 요구 사항을 충족하는 노드에 워크로드를 배치할 수 있게 합니다. 

이미지 호환성 명세를 정의하면 컨테이너 작성자가 필요한 호스트 OS 기능을 선언할 수 있어 호환성 요구 사항을 발견하고 프로그래밍할 수 있습니다. 이 명세는 Kubernetes Node Feature Discovery 프로젝트에 구현되어 있으며, 컨테이너 이미지를 이미지 레지스트리에서 호환성 명세와 함께 지원합니다. 이러한 호환성 명세는 이미지가 특정 환경에서 실행 가능한지 빠르게 평가할 수 있게 합니다. 

결론적으로, Kubernetes에 이미지 호환성을 추가함으로써 미션 크리티컬 워크로드가 호스트 OS 요구 사항을 더 효율적으로 정의하고 검증할 수 있게 되었습니다. 앞으로 이러한 호환성 메타데이터의 채택은 전문화된 컨테이너화된 애플리케이션의 신뢰성과 성능을 크게 향상시킬 것입니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/06/25/image-compatibility-in-cloud-native-environments/)

## 🔹 Spring Boot - Spring Cloud 2023.0.6 (aka Leyton) Has Been Released
Spring Cloud 2023.0.6 (Leyton) 버전이 정식으로 출시되었습니다. 이번 릴리스는 Spring Boot 3.3.13을 기반으로 하며, 여러 버그 수정과 개선 사항이 포함되어 있습니다. 2023.0.x 버전은 이번이 마지막 오픈 소스 릴리스이며, 2025년 7월 1일부터 상업적 지원만 제공될 예정입니다. 주요 변경 사항으로는 Spring Cloud Gateway의 httpClient connectTimeout 설정 재로드 지원, Spring Cloud Circuitbreaker의 openTimeout 및 resetTimeout 사용자 지정 기능 추가 등이 있습니다. Maven Central에서 다운로드할 수 있으며, 자세한 변경 사항은 GitHub 프로젝트에서 확인할 수 있습니다. 개발자들은 피드백을 GitHub, Gitter, Stack Overflow, Twitter를 통해 제공할 수 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/06/27/spring-cloud-2023-0-6-released)

## 🔹 Docker - Building an Easy Private AI Assistant with Goose and Docker Model Runner
이 기술 블로그 글은 Goose와 Docker Model Runner를 사용하여 개인 AI 비서를 구축하는 방법을 설명합니다. Goose는 AI 모델을 사용해 개발 작업을 자동화하는 혁신적인 CLI 도구이며, Docker Model Runner는 Docker를 통해 AI 모델을 로컬에서 쉽게 배포할 수 있도록 합니다. 이 두 기술을 결합하면 고급 AI 지원 기능을 갖춘 강력한 로컬 개발 환경이 만들어져 코딩과 자동화에 이상적입니다. 로컬에서 AI 기반 개발 작업을 원활하게 실행하고자 할 때 유용한 방법을 제시합니다.
👉 [자세히 보기](https://www.docker.com/blog/building-an-ai-assistant-with-goose-and-docker-model-runner/)

## 🔹 Java - Project Leyden’s AOT - Shifting Java Startup into High Gear
Project Leyden은 Java 프로그램의 시작 시간을 단축하고 성능이 최고조에 도달하는 시간을 줄이며 프로그램의 메모리 사용량을 개선하는 것을 목표로 하고 있습니다. 이를 위해 프로그램 시작 단계에서의 작업을 선택적으로 미리 수행하여, 이전 실행과 유사한 미래 실행이 있을 것이라는 가정하에 작업을 사전에 처리합니다. 이 블로그에서는 Leyden이 어떻게 이러한 작업을 미리 수행하여 Java 프로그램의 효율성을 높이는지를 탐구합니다.
👉 [자세히 보기](https://inside.java/2025/06/29/javaone-leyden-aot/)

## 🔹 Golang - [ On | No ] syntactic support for error handling
Go 팀이 오류 처리 지원에 대한 계획을 논의하고 있습니다. 이 블로그 글에서는 Go 언어에서의 오류 처리에 대한 문법적 지원 여부에 대한 내용이 다루어집니다.
👉 [자세히 보기](https://go.dev/blog/error-syntax)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
제목: KubeCon + CloudNativeCon EU '25에서의 헬름

요약: 헬름 팀이 2025년 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU에 참가합니다. 올해 말 출시 예정인 헬름 4에 대한 논의에 참여할 수 있는 기회가 제공되며, 헬름 부스와 발표 세션에서 유지 관리 팀과의 대화에 참여할 수 있습니다. 주간 동안 진행될 모든 헬름 관련 활동에 대한 자세한 내용은 링크를 통해 확인하세요.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

