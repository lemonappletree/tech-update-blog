# 🛠️ 2025-12-02 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.35 Sneak Peek
이 글은 곧 출시될 Kubernetes v1.35의 주요 변경 사항을 소개합니다. 이번 릴리스에서는 몇 가지 기능이 폐기되거나 대체됩니다. cgroup v1 지원이 제거되고, kube-proxy의 ipvs 모드가 폐기될 예정입니다. 또한, containerd v1.y의 지원도 중단되므로, 사용자는 containerd 2.0 이상으로 업그레이드해야 합니다. 새로운 기능으로는 노드가 지원하는 기능을 명시적으로 선언하는 '노드 선언 기능', Pod 리소스의 '즉시 업데이트', Pod 인증서, taints의 수치적 비교 지원, 사용자 네임스페이스 및 OCI 이미지를 볼륨으로 마운트하는 지원 등이 있습니다. Kubernetes v1.35 릴리스는 2025년 12월 17일로 예정되어 있으며, 다양한 커뮤니티 활동을 통해 더 많은 정보를 얻을 수 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/11/26/kubernetes-v1-35-sneak-peek/)

## 🔹 Spring Boot - Towards Spring Tools 5 - Stereotypes and a new Structural View
이 블로그 글에서는 Spring 프로젝트에서 개발자가 사용하는 고수준 추상 개념들을 중심으로 Spring Tools가 어떻게 소스 코드를 분석하고 개발자에게 더 나은 코딩 환경을 제공하는지를 설명합니다. Spring Tools는 기존의 "Go To Symbol" 기능을 활용해 이러한 개념들을 심벌로 만들어 개발자가 프로젝트 내에서 빠르게 탐색하고 검색할 수 있도록 했습니다. 

새로운 주요 릴리스에서는 jMolecules 2.0의 스테레오타입 개념을 통합하여 프로젝트의 논리적 구조를 시각화하는 기능을 도입했습니다. 이 구조적 뷰는 프로젝트 파일과 폴더 대신, 웹 컨트롤러, 설정 클래스, 요청 매핑, 저장소, 엔티티 같은 스테레오타입에 따라 요소들을 그룹화하여 보여줍니다. 

사용자는 자신만의 스테레오타입을 정의할 수도 있으며, Spring Modulith를 사용하는 경우 모듈 구조도 논리적 구조 뷰에 자동으로 반영됩니다. 이러한 기능들은 개발자가 프로젝트를 더 잘 이해하고 관리할 수 있도록 도와줍니다. 블로그는 또한 사용자에게 Spring Tools 5의 최신 릴리스 후보를 시도해볼 것을 권장합니다.
👉 [자세히 보기](https://spring.io/blog/2025/11/28/towards-spring-tools-5-part2)

## 🔹 Docker - Run Embedding Models and Unlock Semantic Search with Docker Model Runner
기술 블로그 글은 임베딩 모델과 Docker Model Runner를 활용한 의미 검색에 관한 내용입니다. 임베딩은 현대 AI 응용 프로그램의 핵심으로, 텍스트, 코드, 문서의 의미를 이해하는 데 도움을 줍니다. 이를 통해 의미 검색, 검색 증강 생성(RAG), 지능형 추천 시스템 등이 가능해집니다. 그러나 임베딩 생성을 위해 호스팅된 API를 사용할 경우 몇 가지 절충이 필요합니다.
👉 [자세히 보기](https://www.docker.com/blog/run-embedding-models-for-semantic-search/)

## 🔹 Java - Agent Orchestration with LangChain4J
LangChain4J는 언어 모델과 AI 워크플로를 Java 애플리케이션에 쉽게 통합할 수 있도록 돕는 라이브러리로, Java 및 기업 AI 커뮤니티에서 주목받고 있습니다. 이 글에서는 Langchain4j-agentic 모듈을 통해 AI 및 비AI 에이전트를 강력하고 통제된 워크플로로 결합하는 방법을 소개합니다. 주요 패턴으로는 순차, 반복, 조건, 병렬 패턴과 에이전트가 스스로 실행할 작업을 결정하는 감독 패턴이 포함되며, 인간 검증 전략도 다룹니다. 복합 에이전트는 전체 워크플로를 하나의 구성 요소로 묶고, AgenticScope는 컨텍스트에 대한 제어와 호출 체인의 명확한 관점을 제공합니다. 데모를 통해 작은 작업부터 복잡한 자동화까지 확장 가능한 에이전트 시스템을 보여줍니다. AI에 관심이 있거나 코드베이스에서 실험해보고 싶은 Java 개발자는 현재 가능한 것과 통제 방법, 에이전트의 다음 발전을 어떻게 이끌 수 있는지를 이해할 수 있습니다.
👉 [자세히 보기](https://inside.java/2025/12/01/devoxxbelgium-langchain4j-keynote/)

## 🔹 Golang - Go’s Sweet 16
블로그 글 "Go’s Sweet 16"은 프로그래밍 언어 Go의 16번째 생일을 축하하는 내용입니다. 글에서는 Go 언어의 탄생과 발전 과정을 되돌아보고, 그동안의 성과와 커뮤니티의 성장을 기념합니다. Go 언어가 개발자들에게 제공한 장점과 앞으로의 발전 방향에 대해서도 언급하고 있습니다.
👉 [자세히 보기](https://go.dev/blog/16years)

## 🔹 Helm - Helm 4 Released
지난 11월 12일, KubeCon + CloudNativeCon에서 열린 Helm 4 발표 행사에서 Helm v4.0.0이 출시되었습니다. 이는 6년 만에 처음으로 나온 Helm의 주요 신규 버전입니다.
👉 [자세히 보기](https://helm.sh/blog/helm-4-released)

