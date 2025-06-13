# 🛠️ 2025-06-13 기술 업데이트 요약

## 🔹 Kubernetes - Enhancing Kubernetes Event Management with Custom Aggregation
이 블로그 글은 Kubernetes 이벤트 관리를 개선하기 위한 맞춤형 이벤트 집계 시스템 구축 방법을 설명합니다. Kubernetes 클러스터에서 이벤트는 다양한 작업에 대해 생성되며, 이는 디버깅과 모니터링에 중요하지만, 대규모 클러스터에서는 이벤트 관리 및 분석이 어려워집니다. 

주요 문제점으로는 이벤트의 대량 생성, 제한된 보존 시간, 관련 이벤트 간의 자동 연계 부족, 표준화된 심각도 및 분류의 부재, 유사 이벤트의 자동 그룹화 부족 등이 있습니다. 

맞춤형 이벤트 집계 시스템은 이러한 문제를 해결하고, 엔지니어링 팀이 클러스터 동작을 더 잘 이해하고 문제를 효율적으로 해결할 수 있게 돕습니다. 시스템은 이벤트를 모니터링하고, 처리 및 분류하며, 장기 보존을 위한 저장소를 사용합니다. 

이 블로그는 Go 프로그래밍 언어를 사용하여 이벤트 집계 시스템의 아키텍처와 구현 방법을 예시로 제공하며, 추가적으로 패턴 감지 및 실시간 경고 기능 구현을 제안합니다. 이를 통해 클러스터의 가시성을 높이고 문제 해결 시간을 단축할 수 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/06/10/enhancing-kubernetes-event-management-custom-aggregation/)

## 🔹 Spring Boot - Spring Framework 7.0.0-M6 available now
Spring Framework 7.0.0-M6 버전이 출시되었습니다. 이번 마일스톤에서는 이전 버전들(M1~M5)에서 제공된 기능들을 개선하고 새로운 기능을 추가했습니다. 주요 변경 사항 중 하나는 Spring Core에 포함된 재시도 지원 기능입니다. 이는 불필요한 기능을 제거하고 API를 재검토하여 "spring-core" 모듈에 통합한 것입니다. 이를 통해 Spring Batch와 같은 프로젝트에서 spring-retry 대신 사용할 수 있도록 준비 중입니다. 자세한 변경 사항과 업그레이드 관련 정보는 변경 로그와 7.0 릴리즈 노트를 통해 확인할 수 있으며, 해당 버전은 Maven Central 및 Spring의 저장소에서 다운로드 가능합니다.
👉 [자세히 보기](https://spring.io/blog/2025/06/12/spring-framework-7-0-0-M6-available-now)

## 🔹 Docker - How to Build, Run, and Package AI Models Locally with Docker Model Runner
이 기술 블로그는 AI 모델을 로컬 환경에서 실행하고 패키징하는 방법을 설명합니다. 글을 쓴 저자는 숙련된 DevOps 엔지니어이자 Docker Captain으로, 다양한 산업에서 AI 시스템 구축을 지원해왔습니다. 블로그에서는 Docker Model Runner라는 가볍고 개발자 친화적인 도구를 사용하여 로컬 AI 모델을 실행하고 패키징하는 과정을 안내합니다. AI 기능이 현대 인프라의 핵심이라는 점을 강조하며, Docker Model Runner를 활용한 실용적인 방법을 소개합니다.
👉 [자세히 보기](https://www.docker.com/blog/how-to-build-run-and-package-ai-models-locally-with-docker-model-runner/)

## 🔹 Java - FFM vs. Unsafe. Safety (Sometimes) Has a Cost
이 블로그 글에서는 Foreign Function & Memory(FFM) API가 Unsafe보다 더 안전하면서도 거의 동일한 속도를 제공한다고 설명합니다. FFM API는 외부 함수 호출과 메모리 관리를 보다 안전하게 수행할 수 있도록 설계되었습니다. 이는 시스템의 안정성과 보안을 강화하는 데 기여하지만, 때로는 성능에 약간의 비용이 따를 수 있습니다.
👉 [자세히 보기](https://inside.java/2025/06/12/ffm-vs-unsafe/)

## 🔹 Golang - [ On | No ] syntactic support for error handling
이 블로그 글은 Go 언어 팀이 오류 처리 지원을 위한 구문적 지원 계획에 대해 논의하는 내용을 다루고 있습니다. 현재 Go 언어에서는 오류 처리를 위한 특별한 구문적 지원이 없으며, 이에 대한 개선 방안 및 계획을 소개하고 있습니다. 팀은 오류 처리를 더 간편하고 효율적으로 만들기 위한 다양한 접근 방식을 검토하고 있습니다.
👉 [자세히 보기](https://go.dev/blog/error-syntax)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
블로그 글 요약: Helm 팀이 2025년 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU에 참가합니다. 올해 말 출시 예정인 Helm 4에 대한 논의에 참여하고 싶다면, 발표 세션과 프로젝트 파빌리온의 Helm 부스를 방문해 보세요. 주간 동안 진행되는 모든 Helm 관련 활동에 대한 자세한 내용은 블로그를 참조하세요.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

