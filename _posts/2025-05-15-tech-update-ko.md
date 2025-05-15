# 🛠️ 2025-05-15 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.33: Updates to Container Lifecycle
Kubernetes v1.33은 컨테이너 라이프사이클에 대한 몇 가지 업데이트를 도입했습니다. 이제 컨테이너 라이프사이클 훅의 Sleep 액션은 0초의 대기 시간을 지원하며, 이는 기본적으로 활성화되어 있습니다. 또한 컨테이너가 종료될 때 전송되는 종료 신호를 사용자 정의할 수 있는 알파 지원이 추가되었습니다.

기존의 Sleep 액션은 Kubernetes v1.30부터 기본적으로 활성화되어 있으며, v1.33에서는 0초 대기 시간을 설정할 수 있습니다. 또한, 새로운 기능인 ContainerStopSignals는 컨테이너 사양에서 사용자 정의 종료 신호를 지정할 수 있도록 Kubernetes API에 추가되었습니다. 이를 통해 사용자는 컨테이너 이미지에 지정된 기본 종료 신호를 재설정하거나 운영 체제에 맞는 유효한 종료 신호를 사용할 수 있습니다.

이 기능들은 SIG Node에 의해 추진되며, 관심 있는 사람들은 SIG Node에 참여하여 개발에 기여하거나 의견을 나눌 수 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/05/14/kubernetes-v1-33-updates-to-container-lifecycle/)

## 🔹 Spring Boot - Spring AI 1.0.0 RC1 Released
이 블로그 글은 Spring AI 1.0.0 RC1 버전의 출시를 알리는 내용입니다. 이 버전은 최종 수정, 버그 수정 및 새로운 기능이 포함되어 있으며, 공식 출시일은 2025년 5월 20일로 예정되어 있습니다. 이 기간 동안 문서 개선과 버그 해결에 집중할 예정입니다. 또한, AI 생성 음악 플레이리스트에 새로운 곡이 추가되었음을 알리며, 블로그 읽기와 코딩 경험을 향상시킬 수 있도록 안내합니다.

주요 변경 사항으로는 채팅 클라이언트와 어드바이저의 키 이름 변경, 독립 템플릿 사용, 채팅 메모리 저장소 명명 표준화, 관측성 변경 등이 있습니다. 새 기능으로는 모델 향상, RAG 및 문서 처리, 도구 호출, 메모리 관리 및 관측성 개선 기능이 포함됩니다. 여러 기여자들이 리팩토링, 버그 수정, 문서 개선에 참여했습니다.
👉 [자세히 보기](https://spring.io/blog/2025/05/13/spring-ai-1-0-0-RC1-released)

## 🔹 Docker - Securing Model Context Protocol: Safer Agentic AI with Containers
제목: 모델 컨텍스트 프로토콜 보안: 컨테이너를 활용한 더 안전한 에이전틱 AI

요약: 모델 컨텍스트 프로토콜(MCP) 도구는 주로 초기 사용자들에게 사용되고 있지만, 더 넓은 범위로의 채택이 가속화되고 있습니다. 이와 함께 MCP의 보안 문제도 더욱 긴급해지고 있습니다. 에이전트의 자율성을 높임으로써, MCP 도구는 사용자 기대와 에이전트 행동 간의 불일치 및 통제되지 않은 실행과 관련된 새로운 위험을 초래합니다. 이러한 시스템은 또한 새로운 문제를 제시합니다.
👉 [자세히 보기](https://www.docker.com/blog/whats-next-for-mcp-security/)

## 🔹 Java - Garbage Collection in Java: The Performance Benefits of Upgrading
이 기술 블로그 글은 자바 플랫폼의 핵심 기능인 가비지 컬렉션(GC)에 대해 다룹니다. GC는 자동 메모리 관리의 한 형태로, 개발자들이 저수준 메모리 관리 문제보다 애플리케이션 로직에 집중할 수 있도록 도와줍니다. 이 글에서는 GC의 기본 개념, 사용 가능한 GC 알고리즘과 그 차이점, 적절한 GC 선택의 이점, 그리고 최신 JDK로 업그레이드했을 때의 성능 향상에 대해 설명합니다.
👉 [자세히 보기](https://inside.java/2025/05/14/javaone-garbage-collection/)

## 🔹 Golang - More predictable benchmarking with testing.B.Loop
이 기술 블로그 글은 Go 1.24 버전에서 개선된 벤치마크 루프 기능에 대해 설명하고 있습니다. 새로운 `testing.B.Loop` 메서드는 벤치마크 테스트를 더 예측 가능하고 안정적으로 만드는 데 초점을 맞추고 있습니다. 이를 통해 개발자는 성능 테스트를 보다 효율적으로 수행할 수 있습니다.
👉 [자세히 보기](https://go.dev/blog/testing-b-loop)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
제목: Helm @ KubeCon + CloudNativeCon EU '25

내용: Helm 팀이 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU '25에 참가합니다. 올해 말 출시 예정인 Helm 4에 대한 논의가 진행될 예정이니, 발표 세션과 프로젝트 파빌리온 내 Helm 부스에서 유지 관리자들과의 대화에 참여해 보세요. 행사 주간 동안 Helm과 관련된 활동에 대한 자세한 내용을 확인할 수 있습니다.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

