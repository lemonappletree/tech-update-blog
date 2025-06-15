# 🛠️ 2025-06-15 기술 업데이트 요약

## 🔹 Kubernetes - Enhancing Kubernetes Event Management with Custom Aggregation
이 블로그 글은 Kubernetes 이벤트 관리의 어려움을 해결하기 위해 커스텀 이벤트 집계 시스템을 구축하는 방법을 설명하고 있습니다. Kubernetes 클러스터에서 발생하는 다양한 이벤트는 디버깅과 모니터링에 유용하지만, 대규모 클러스터에서는 수천 개의 이벤트가 생성되어 관리가 어렵습니다. 글은 이벤트 볼륨, 보존 기간, 상관관계, 분류 및 집계의 문제를 지적하고, 커스텀 시스템 구축을 통해 이를 해결하는 방법을 제안합니다. 

커스텀 시스템은 이벤트를 모니터링, 처리, 저장하는 세 가지 주요 구성 요소로 구성되며, Go 언어를 사용하여 구현합니다. 이러한 시스템은 이벤트를 그룹화하고 상관관계를 파악하여 문제를 신속하게 해결하는 데 도움을 줍니다. 이를 통해 문제 해결 시간을 단축하고, 시스템 신뢰성을 높일 수 있습니다. 

또한, 이벤트 처리 및 분류, 상관관계 구현, 이벤트 저장 및 보존에 대한 구체적인 구현 방법과 모범 사례도 제시하고 있습니다. 마지막으로 미래 개선 사항으로 머신러닝을 통한 이상 탐지, 관찰 플랫폼과의 통합 등을 제안합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/06/10/enhancing-kubernetes-event-management-custom-aggregation/)

## 🔹 Spring Boot - Spring Data 2025.0.1, 2024.1.7, and 2024.0.13 released
이 기술 블로그 글은 Spring Data의 새로운 서비스 릴리스인 2025.0.1, 2024.1.7, 2024.0.13의 출시를 알리고 있습니다. 이번 릴리스에는 의존성 업그레이드, 회귀 오류 수정 및 선택된 개선 사항이 포함되어 있습니다. 특히, 2024.0.13 릴리스는 오픈 소스 종료 시점에 도달했으므로 최신 3.4.x 버전으로의 업그레이드를 권장하고 있습니다. 또한, 곧 출시될 Spring Boot 릴리스가 이 새로운 릴리스를 반영할 예정입니다. 각 릴리스마다 다양한 Spring Data 모듈의 버전과 관련 문서, 변경 로그에 대한 링크가 제공됩니다.
👉 [자세히 보기](https://spring.io/blog/2025/06/13/spring-data-2025-0-1-2024-1-7-and-2024-0-13-released)

## 🔹 Docker - How to Build, Run, and Package AI Models Locally with Docker Model Runner
이 기술 블로그 글은 AI 시스템 구축 경험이 풍부한 DevOps 엔지니어가 로컬에서 AI 모델을 실행하고 패키징하는 방법을 설명합니다. 특히, Docker Model Runner라는 가볍고 개발자 친화적인 도구를 사용하여 현대 인프라에 필수적인 AI 기능을 어떻게 구현할 수 있는지에 대한 가이드를 제공합니다.
👉 [자세히 보기](https://www.docker.com/blog/how-to-build-run-and-package-ai-models-locally-with-docker-model-runner/)

## 🔹 Java - Interconnecting Java and Native Code with the FFM API
제목: FFM API로 Java와 네이티브 코드 연결하기  
요약: Java SE 22에 도입된 Foreign Function & Memory Access API (FFM API)는 Java 애플리케이션과 네이티브 라이브러리 간의 불일치를 세 단계로 줄였습니다. 첫째, FFM API는 오프힙 메모리의 영역을 메모리 세그먼트로 모델링할 수 있는 풍부한 API를 제공합니다. 둘째, 네이티브 함수를 설명하고 연결할 수 있는 API도 제공합니다. 셋째, jextract라는 도구를 사용하여 이러한 라이브러리에 접근하는 데 필요한 FFM API 아티팩트를 자동으로 생성함으로써 네이티브 라이브러리 접근을 더욱 간소화할 수 있습니다. 이 프레젠테이션은 FFM의 기본 원칙과 네이티브 그래픽 라이브러리 및 AI 프레임워크와의 Java 통합을 보여줍니다.
👉 [자세히 보기](https://inside.java/2025/06/14/javaone-ffm/)

## 🔹 Golang - [ On | No ] syntactic support for error handling
블로그 글에서는 Go 팀이 오류 처리에 대한 문법적 지원 계획을 논의하고 있다는 내용을 다루고 있습니다. Go 언어에서의 오류 처리 방식을 개선하기 위한 다양한 아이디어와 접근 방식이 검토되고 있으며, 이러한 변화가 언어에 어떤 영향을 미칠지에 대한 논의가 이루어지고 있습니다.
👉 [자세히 보기](https://go.dev/blog/error-syntax)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
블로그 글 요약: Helm 팀이 2025년 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU '25에 참가합니다. 올해 말 출시 예정인 Helm 4에 관한 논의에 참여하고자 한다면, 이번 행사에서 Helm 유지관리자들과의 토크 세션 및 Helm 부스를 방문해 보세요. 행사 주간 동안 진행되는 Helm 관련 활동에 대한 자세한 내용은 링크를 통해 확인할 수 있습니다.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

