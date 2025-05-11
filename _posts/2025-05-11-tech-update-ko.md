# 🛠️ 2025-05-11 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.33: Streaming List responses
이 블로그 글은 Kubernetes v1.33의 새로운 기능인 스트리밍 인코딩을 소개합니다. 기존에는 대규모 클러스터에서 큰 데이터 세트를 처리하는 List 요청이 클러스터의 안정성에 부정적 영향을 줄 수 있었습니다. 새로운 스트리밍 인코딩 방식은 List 응답의 메모리 소비를 줄이고 API 서버의 안정성을 높입니다. 이는 메모리 사용량을 크게 줄이고, 더 많은 동시 요청과 큰 데이터 세트를 처리할 수 있게 하여 OOM(Out-of-Memory) 위험과 서비스 중단을 감소시킵니다. 벤치마크 결과, 메모리 사용량이 최대 20배 줄어드는 성과를 보였습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/05/09/kubernetes-v1-33-streaming-list-responses/)

## 🔹 Spring Boot - A Bootiful Podcast: V Körbes on security from the platform on up
제목: 아름다운 팟캐스트: 플랫폼부터 시작하는 보안에 대한 V Körbes와의 대화

요약: 안녕하세요, Spring 팬 여러분! 오늘의 특별한 에피소드에서는 Broadcom의 V Körbes와 함께 애플리케이션 위아래에서의 보안에 대한 이야기를 나눕니다.
👉 [자세히 보기](https://spring.io/blog/2025/05/08/a-bootiful-podcast-v-korbes)

## 🔹 Docker - Securing Model Context Protocol: Safer Agentic AI with Containers
블로그 글은 "모델 컨텍스트 프로토콜(MCP): 컨테이너를 활용한 안전한 에이전트 AI"라는 주제로, MCP 도구가 초기에 소수의 사용자에게만 사용되었지만 점차 더 널리 채택되고 있다고 설명합니다. 이와 함께 MCP의 보안 문제도 더욱 중요해지고 있습니다. 에이전트의 자율성이 증가함에 따라 사용자 기대와 에이전트 행동 간의 불일치 및 통제되지 않은 실행과 관련된 새로운 위험이 발생할 수 있습니다. 이러한 시스템은 새로운 형태의 보안 문제를 일으킬 가능성도 있습니다.
👉 [자세히 보기](https://www.docker.com/blog/whats-next-for-mcp-security/)

## 🔹 Java - JavaFX 24 and Beyond
"JavaFX 24와 그 이후"라는 제목의 기술 블로그 글은 JavaFX의 최신 버전인 JavaFX 24에 대한 내용을 다루고 있습니다. JavaFX는 데스크톱 및 모바일 애플리케이션을 구축하기 위한 강력한 그래픽 UI 도구이며, 최근 몇 년간 개발된 새로운 기능들을 소개합니다. 주요 기능으로는 RichTextArea(인큐베이터), CSS 전환, 플랫폼 환경 설정 등이 있습니다. 또한, 여러 데모와 샘플 코드도 제공됩니다. 앞으로 JavaFX에 추가될 기능에 대한 예고도 포함되어 있습니다.
👉 [자세히 보기](https://inside.java/2025/05/10/javaone-javafx/)

## 🔹 Golang - More predictable benchmarking with testing.B.Loop
이 블로그 글은 Go 1.24에서 향상된 벤치마크 루프 기능인 `testing.B.Loop`에 대해 다루고 있습니다. 새로운 기능은 더 예측 가능한 벤치마킹 결과를 제공하며, 개발자들이 벤치마크 테스트를 보다 효율적으로 수행할 수 있도록 돕습니다. 이를 통해 정확한 성능 측정이 가능해지고, 코드 최적화에 유리한 환경을 제공합니다.
👉 [자세히 보기](https://go.dev/blog/testing-b-loop)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
블로그 글 요약: Helm 팀이 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU '25에 참가합니다. 올해 말 출시 예정인 Helm 4와 관련된 대화에 참여하고 싶다면, 발표 세션과 Helm 부스를 방문해보세요. 주간 동안 진행될 Helm 관련 활동에 대한 자세한 내용은 아래 링크에서 확인할 수 있습니다.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

