# 🛠️ 2025-06-06 기술 업데이트 요약

## 🔹 Kubernetes - Introducing Gateway API Inference Extension
이 기술 블로그 글은 Kubernetes에서 현대적인 생성 AI 및 대형 언어 모델(LLM) 서비스에 적합한 Gateway API Inference Extension을 소개합니다. LLM 추론 세션은 자원이 많이 소모되고 상태를 일부 유지해야 하는 특성이 있어 기존의 짧고 상태가 없는 웹 요청과는 다른 트래픽 라우팅 문제가 발생합니다. 이 확장은 이러한 문제를 해결하기 위해 기존 Gateway API에 추론 전용 라우팅 기능을 추가하여 GenAI/LLM을 '모델-서비스' 접근 방식으로 자체 호스팅할 수 있도록 합니다. 

Inference Extension은 모델 인식 라우팅, 요청 중요도 지원, 안전한 모델 롤아웃, 그리고 실시간 모델 메트릭 기반의 로드 밸런싱 최적화를 목표로 합니다. 이를 통해 AI 워크로드의 지연 시간을 줄이고 GPU 활용도를 향상시키고자 합니다. InferencePool과 InferenceModel이라는 두 개의 새로운 사용자 정의 리소스를 도입하여 AI/ML 서비스 워크플로우 내의 특정 사용자 역할에 맞게 설계되었습니다. 

이 확장은 모델-인식 라우팅을 통해 GPU 기반 LLM 워크로드의 지연 시간을 크게 줄이는 데 기여합니다. 앞으로는 원격 캐시를 위한 프리픽스 캐시 인식 로드 밸런싱, 자동 롤아웃을 위한 LoRA 어댑터 파이프라인 등 다양한 기능이 추가될 예정입니다. 이 프로젝트는 Kubernetes-native 도구와 모델 서빙을 맞춰 AI/ML 트래픽 라우팅을 간소화하고 표준화하는 것을 목표로 합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/06/05/introducing-gateway-api-inference-extension/)

## 🔹 Spring Boot - A Bootiful Podcast: IntelliJ IDEA lead Aleksey Stukalov
이번 블로그 글에서는 스프링 팬들을 위해 IntelliJ IDEA의 리드인 Aleksey Stukalov와의 인터뷰를 소개합니다.
👉 [자세히 보기](https://spring.io/blog/2025/06/05/a-bootiful-podcast-aleksey-stukalov)

## 🔹 Docker - Settings Management for Docker Desktop now generally available in the Admin Console
Docker Desktop의 설정 관리 기능이 이제 관리자 콘솔에서 일반적으로 사용 가능하게 되었습니다. 이 기능은 Docker Business 구독을 가진 고객들이 관리자 콘솔에서 구성할 수 있습니다. 초기 액세스 기간을 성공적으로 마친 후, 이 강력한 관리 솔루션은 새로운 컴플라이언스 보고 기능이 추가되면서 중앙 집중식 Docker Desktop 관리를 향한 우리의 비전을 완성했습니다.
👉 [자세히 보기](https://www.docker.com/blog/settings-management-for-docker-desktop-now-generally-available-in-the-admin-console/)

## 🔹 Java - Java 25 Brings 18 JEPs 😱 Inside Java Newscast #92
Java 25는 9월 16일에 출시될 예정이며, 오늘 기능 세트가 확정되었습니다. 이번 업데이트는 언어, API 및 런타임에서 11개의 완성된 기능과 7개의 개발 중인 기능이 포함되어 있어 주목할 만합니다. 다음 장기 지원 릴리스는 빠른 업데이트가 필요할 정도로 가치가 있을 것입니다.
👉 [자세히 보기](https://inside.java/2025/06/05/newscast-92/)

## 🔹 Golang - [ On | No ] syntactic support for error handling
블로그 글에서는 Go 팀이 오류 처리에 대한 구문 지원을 계획하고 있다는 내용을 다룹니다. Go 언어의 오류 처리 방식에 대한 개선을 논의하며, 이를 위한 새로운 구문 도입 가능성을 검토하고 있습니다. 이 글은 이러한 변화의 배경과 방향성에 대한 개요를 제공합니다.
👉 [자세히 보기](https://go.dev/blog/error-syntax)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
블로그 글 요약: Helm 팀이 2025년 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU '25에 참석합니다. 올해 말 출시 예정인 Helm 4와 관련된 대화에 참여하고 싶다면, 발표 세션과 Project Pavilion에 있는 Helm 부스를 방문하세요. 행사 주간 동안 Helm과 관련된 모든 활동의 자세한 내용은 링크를 통해 확인할 수 있습니다.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

