# 🛠️ 2025-08-02 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.34 Sneak Peek
Kubernetes v1.34는 2025년 8월 말에 출시될 예정이며, 기존 기능의 제거나 폐지는 없지만 다수의 개선 사항이 포함될 예정입니다. 주요 기능으로는 다음과 같습니다:

1. **DRA(동적 자원 할당) 핵심 안정화**: GPU나 맞춤형 하드웨어를 유연하게 사용할 수 있게 해주는 DRA가 안정화 단계로 졸업할 예정입니다.

2. **이미지 풀 인증을 위한 ServiceAccount 토큰**: kubelet이 컨테이너 이미지 레지스트리에서 인증을 받을 때 ServiceAccount 토큰을 사용할 수 있게 됩니다.

3. **디플로이먼트를 위한 Pod 교체 정책**: 디플로이먼트 변경 시 새로운 Pod 생성 시점을 제어할 수 있는 기능이 도입됩니다.

4. **kubelet 및 API 서버의 프로덕션급 트레이싱**: OpenTelemetry 표준을 사용하여 kubelet과 API 서버의 트레이싱 기능이 강화됩니다.

5. **서비스의 트래픽 배포**: PreferSameZone 및 PreferSameNode 옵션으로 트래픽 배포를 제어할 수 있습니다.

6. **KYAML 지원**: Kubernetes 전용 YAML 서브셋인 KYAML이 도입되어, 안전하고 명확한 매니페스트 작성이 가능해집니다.

7. **HPA의 세밀한 자동 확장 제어**: HPA의 스케일링 허용값을 더 세밀하게 설정할 수 있는 기능이 추가됩니다.

Kubernetes 커뮤니티에 참여하거나 더 많은 정보를 얻고 싶다면 SIGs에 참여하거나 커뮤니티 미팅에 참석할 수 있습니다. Kubernetes v1.34는 2025년 8월 27일에 공식 발표될 예정입니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/07/28/kubernetes-v1-34-sneak-peek/)

## 🔹 Spring Boot - A Bootiful Podcast: Spring Security lead Rob Winch on Spring Security 7.0, SpringOne 2025, and more
이 기술 블로그 글은 Spring Security의 리더인 Rob Winch와 함께하는 팟캐스트 에피소드를 소개합니다. 여기서 그들은 2025년 11월에 출시될 Spring Security 7.0의 새로운 기능에 대해 논의하고, SpringOne 2025에서의 발표 내용에 대해 설명합니다. SpringOne 2025에 대한 등록 링크도 포함되어 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/07/31/a-bootiful-podcast-rob-winch)

## 🔹 Docker - GenAI vs. Agentic AI: What Developers Need to Know
제목: 생성 AI vs. 에이전틱 AI: 개발자가 알아야 할 것

요약: 생성 AI(GenAI)와 그 뒤의 모델들은 이미 개발자들이 코드를 작성하고 애플리케이션을 구축하는 방식을 변화시켰습니다. 그러나 새로운 인공지능의 유형이 등장하고 있는데, 그것이 바로 에이전틱 AI입니다. 생성 AI가 콘텐츠 생성에 초점을 맞추는 반면, 에이전틱 시스템은 계획을 세우고, 추론하며, 여러 단계에 걸쳐 행동을 취할 수 있어 지능적이고 목표 지향적인 새로운 방식의 구축을 가능하게 합니다.
👉 [자세히 보기](https://www.docker.com/blog/genai-vs-agentic-ai/)

## 🔹 Java - HTTP/3 in Java - Inside Java Newscast #96
블로그 글에서는 JEP 517을 통해 Java의 HTTP Client가 HTTP/3와 호환되도록 업데이트하는 제안을 다루고 있습니다. HTTP/3는 지연 시간이 적고, 빠르게 로드되며 네트워크 혼잡을 줄여주는 장점이 있으며 현재 약 3분의 1의 웹사이트에서 사용되고 있습니다. API 변경은 최소화되었으며 대부분의 작업은 내부적으로 이루어집니다. 이러한 변화는 향후 많은 개선의 기회를 열어줍니다.
👉 [자세히 보기](https://inside.java/2025/07/31/newscast-96/)

## 🔹 Golang - The FIPS 140-3 Go Cryptographic Module
블로그 글 요약: Go 프로그래밍 언어는 이제 FIPS 140-3 표준을 준수하는 네이티브 암호화 모드를 내장하게 되었습니다. 이를 통해 보안 요구사항을 충족해야 하는 애플리케이션에서 Go를 보다 쉽게 사용할 수 있게 되었습니다.
👉 [자세히 보기](https://go.dev/blog/fips140)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
제목: 헬름 @ KubeCon + CloudNativeCon EU '25

요약: 헬름 팀이 2025년 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU에 참가합니다. 올해 말 출시 예정인 Helm 4에 대한 대화에 참여할 수 있는 기회가 제공되며, 헬름 유지보수자들과의 토크 세션 및 프로젝트 파빌리온 내 헬름 부스에서 다양한 활동이 있을 예정입니다. 자세한 내용은 블로그 글을 참고하세요.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

