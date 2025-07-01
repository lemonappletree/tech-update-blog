# 🛠️ 2025-07-01 기술 업데이트 요약

## 🔹 Kubernetes - Image Compatibility In Cloud Native Environments
클라우드 네이티브 환경에서 이미지 호환성은 통신, 고성능 또는 AI 컴퓨팅과 같은 엄격한 성능 기준을 충족해야 하는 산업에서 중요합니다. 컨테이너화된 애플리케이션은 특정 운영체제 구성이나 하드웨어의 존재가 필요할 수 있습니다. Open Container Initiative(OCI)가 존재함에도 불구하고, 이러한 호환성 요구 사항을 표현하는 데에는 여전히 공백이 있습니다. 이를 해결하기 위해 쿠버네티스의 Node Feature Discovery(NFD) 프로젝트가 구현되었습니다. NFD는 클러스터 노드의 하드웨어 및 시스템 기능을 자동으로 감지하여, 특정 시스템 요구 사항을 충족하는 노드에 작업을 배치할 수 있도록 돕습니다. 이 글은 이미지 호환성 사양의 필요성과 이를 해결하기 위한 NFD의 구현 및 이미지 호환성 메타데이터의 사용 사례를 설명합니다. 이를 통해 클라우드 네이티브 환경에서의 호환성 문제를 해결하고자 하는 노력이 강조됩니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/06/25/image-compatibility-in-cloud-native-environments/)

## 🔹 Spring Boot - Spring Cloud 2023.0.6 (aka Leyton) Has Been Released
Spring Cloud 2023.0.6 (Leyton) 버전이 공식 출시되었습니다. 이 릴리스는 Maven Central에서 다운로드할 수 있으며, Spring Boot 3.3.13을 기반으로 하고 있습니다. 이번 릴리스에서는 여러 버그가 수정되었으며, 2025년 7월 1일부터는 상업적 지원만 제공될 예정입니다. 주요 변경 사항으로는 Spring Cloud Gateway에서 httpClient connectTimeout 설정의 리로딩 지원과 Spring Cloud Circuitbreaker에서 openTimeout 및 resetTimeout 설정의 사용자 정의 기능 추가 등이 있습니다. 또한, Spring Cloud Contract의 일부 아티팩트는 더 이상 Maven Central에서 제공되지 않으며, Docker 이미지나 소스에서 빌드해야 합니다. 여러 모듈의 버전이 업데이트되었으며, 자세한 내용은 각 모듈의 릴리스 노트를 참고하면 됩니다. 피드백은 GitHub, Gitter, Stack Overflow 또는 Twitter를 통해 받을 수 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/06/27/spring-cloud-2023-0-6-released)

## 🔹 Docker - Tool Calling with Local LLMs: A Practical Evaluation
이 기술 블로그 글은 "로컬 LLM을 사용한 도구 호출: 실용적 평가"라는 주제로, GenAI 및 에이전트 애플리케이션을 구축할 때 어떤 로컬 모델을 도구 호출에 사용해야 하는지에 대한 질문을 다루고 있습니다. Docker와 개발자 커뮤니티 내에서 이러한 질문이 반복적으로 제기된 것을 바탕으로, Docker Model 작업을 시작한 이후로 얻은 통찰을 공유합니다. 이를 통해 적절한 로컬 모델을 선택하는 데 도움을 주고자 합니다.
👉 [자세히 보기](https://www.docker.com/blog/local-llm-tool-calling-a-practical-evaluation/)

## 🔹 Java - Inside Java’s Language Renaissance
"Inside Java’s Language Renaissance"라는 기술 블로그 글은 Java 언어가 더 간단하고 표현력 있으며 데이터 지향적으로 발전하는 과정을 다루고 있습니다. 이 글에서는 Java의 진화 과정과 목표에 대해 설명하며, 언어가 어떻게 발전하고 있는지를 중점적으로 살펴봅니다. Java를 더 이해하기 쉽게 만들고, 개발자들이 보다 효율적으로 코드를 작성할 수 있도록 하기 위한 노력들이 소개됩니다.
👉 [자세히 보기](https://inside.java/2025/06/30/2025-06-30-inside-java-renaissance-part1/)

## 🔹 Golang - [ On | No ] syntactic support for error handling
이 기술 블로그 글은 Go 팀이 오류 처리 지원에 대한 구문적 지원 계획을 논의하는 내용을 담고 있습니다. 블로그에서는 Go 언어에서 오류 처리를 어떻게 개선할지에 대한 다양한 접근법과 그에 따른 장단점을 다루고 있습니다. Go 팀은 오류 처리를 보다 효율적이고 명확하게 하기 위한 방안을 모색 중입니다.
👉 [자세히 보기](https://go.dev/blog/error-syntax)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
블로그 글 요약: Helm 팀이 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU 2025에 참석합니다. 올해 후반에 출시될 Helm 4에 대한 논의가 진행될 예정이니, 발표 세션과 프로젝트 파빌리온의 Helm 부스에서 유지 관리자들과 대화를 나눠보세요. 행사 주간 동안 진행되는 모든 Helm 관련 활동에 대한 자세한 내용은 링크에서 확인할 수 있습니다.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

