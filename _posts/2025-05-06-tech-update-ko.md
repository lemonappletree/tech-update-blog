# 🛠️ 2025-05-06 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.33: Prevent PersistentVolume Leaks When Deleting out of Order graduates to GA
Kubernetes v1.33 버전에서 PersistentVolume(PV) 누수를 방지하는 기능이 정식 출시(GA)되었습니다. 이 기능은 Kubernetes v1.31의 베타 버전으로 처음 소개되었으며, PV가 PVC(PersistentVolumeClaim)보다 먼저 삭제될 경우에도 설정된 삭제 정책이 제대로 작동하도록 개선되었습니다. 이는 파이널라이저를 추가해 스토리지 백엔드에서 자원이 제대로 해제될 때까지 PV가 삭제되지 않도록 함으로써 구현되었습니다. 이 기능을 사용하려면 Kubernetes v1.33 및 외부 프로비저너의 최신 버전을 사용해야 합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/05/05/kubernetes-v1-33-prevent-persistentvolume-leaks-when-deleting-out-of-order-graduate-to-ga/)

## 🔹 Spring Boot - Dynamic Tool Updates in Spring AI's Model Context Protocol
이 블로그 글은 Spring AI의 모델 컨텍스트 프로토콜(MCP)에서 런타임 동안 외부 도구를 동적으로 업데이트하는 기능을 설명합니다. MCP는 표준화된 인터페이스를 통해 AI 모델이 외부 도구와 리소스에 접근할 수 있게 해주며, Spring AI는 이를 통해 AI 애플리케이션의 유연성과 확장성을 제공합니다. 서버는 MCP 도구를 추가하거나 제거할 수 있고, 클라이언트는 이러한 변경 사항을 감지하여 AI 모델에 즉시 반영할 수 있습니다. 이 기능은 기능 플래그 구현, 상황 인식 도구 로딩, 점진적 향상, 동적 플러그인 아키텍처 등 다양한 실용적인 응용 분야에 활용될 수 있습니다. Spring AI는 간단한 API를 통해 이러한 기능을 쉽게 통합할 수 있도록 지원합니다. 관련 코드 예시는 GitHub에서 확인할 수 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/05/04/spring-ai-dynamic-tool-updates-with-mcp)

## 🔹 Docker - Introducing Docker MCP Catalog and Toolkit: The Simple and Secure Way to Power AI Agents with MCP
제목: Docker MCP 카탈로그 및 툴킷 소개: MCP로 AI 에이전트를 간단하고 안전하게 구동하는 방법

요약: 모델 컨텍스트 프로토콜(MCP)은 AI 에이전트가 외부 도구와 연결하는 표준으로 빠르게 자리 잡고 있지만, 개발자 경험은 아직 미흡한 상태입니다. 발견 과정은 단편적이고, 설정은 번거로우며, 보안은 뒤늦게 추가되는 경우가 많습니다. 이러한 경험을 개선하기 위해서는 산업 전반의 노력이 필요합니다. 안전하고 확장 가능하며 신뢰할 수 있는 MCP...
👉 [자세히 보기](https://www.docker.com/blog/announcing-docker-mcp-catalog-and-toolkit-beta/)

## 🔹 Java - Episode 35 “Stream Gatherers” with Viktor Klang
블로그 글 요약: 
에피소드 35에서는 Ana가 JDK 핵심 아키텍트이자 Stream Gatherers JDK 개선 제안서의 저자인 Viktor Klang과 함께 JDK 24의 주요 기능 중 하나인 Gatherers API에 대해 논의합니다.
👉 [자세히 보기](https://inside.java/2025/05/05/podcast-035/)

## 🔹 Golang - More predictable benchmarking with testing.B.Loop
이 기술 블로그 글은 Go 1.24에서 도입된 새로운 기능인 `testing.B.Loop`에 대해 설명합니다. 이 기능은 Go 언어에서 벤치마크 테스트를 더욱 예측 가능하게 만들어 주며, 반복 실행을 통해 보다 정확한 성능 측정을 가능하게 합니다. 이를 통해 개발자는 코드의 성능을 더 신뢰성 있게 평가할 수 있습니다.
👉 [자세히 보기](https://go.dev/blog/testing-b-loop)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
블로그 글 요약: Helm 팀은 2025년 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU에 참가합니다. 올해 말 출시 예정인 Helm 4에 대한 논의에 참여할 수 있는 기회로, 팀의 발표 세션과 프로젝트 파빌리온에 있는 Helm 부스에서 만나볼 수 있습니다. 주간 동안 진행될 Helm 관련 활동에 대한 자세한 내용은 링크를 통해 확인할 수 있습니다.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

