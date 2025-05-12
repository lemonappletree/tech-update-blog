# 🛠️ 2025-05-12 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.33: Streaming List responses
이 블로그 글은 Kubernetes v1.33의 새로운 기능인 "리스트 응답 스트리밍 인코딩"에 대해 설명합니다. 대규모 Kubernetes 클러스터에서 안정성을 유지하기 위해 리스트 요청 처리 시 메모리 소비가 큰 문제가 될 수 있습니다. 기존 방식은 응답 데이터를 한 번에 처리해 메모리를 많이 소비하며, 네트워크 지연 시에도 메모리가 지속적으로 사용됩니다. 새로운 스트리밍 인코더는 리스트 응답의 각 항목을 개별적으로 처리하고 전송하여 메모리 사용을 줄이고, 클러스터의 안정성을 향상시킵니다. 이를 통해 API 서버의 메모리 소비가 예측 가능해지고, 여러 대규모 리스트 요청이 동시에 발생해도 안정성이 유지됩니다. 벤치마크 결과, 메모리 사용량이 70-80GB에서 3GB로 줄어드는 20배의 개선이 있었습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/05/09/kubernetes-v1-33-streaming-list-responses/)

## 🔹 Spring Boot - A Bootiful Podcast: V Körbes on security from the platform on up
안녕하세요, 스프링 팬 여러분! 이번 특별한 에피소드에서는 Broadcom의 V Körbes와 함께 애플리케이션의 상위 및 하위 보안에 대해 이야기합니다.
👉 [자세히 보기](https://spring.io/blog/2025/05/08/a-bootiful-podcast-v-korbes)

## 🔹 Docker - Securing Model Context Protocol: Safer Agentic AI with Containers
제목: 모델 컨텍스트 프로토콜 보안: 컨테이너로 더 안전한 에이전틱 AI

요약: 모델 컨텍스트 프로토콜(MCP) 도구는 주로 초기 사용자들에 의해 사용되고 있지만, 더 널리 확산되고 있는 추세입니다. 이에 따라 MCP 보안 문제도 점점 더 중요해지고 있습니다. 에이전트의 자율성을 높임에 따라, MCP 도구는 사용자 기대와 에이전트 행동 간의 불일치 및 통제되지 않은 실행과 관련된 새로운 위험을 초래합니다. 이러한 시스템은 또한 새로운 형태의 보안 문제를 제시하고 있습니다.
👉 [자세히 보기](https://www.docker.com/blog/whats-next-for-mcp-security/)

## 🔹 Java - JavaFX 24 and Beyond
"JavaFX 24 and Beyond"는 JavaFX의 최신 버전과 향후 발전 방향에 대해 다루는 기술 블로그 글입니다. JavaFX는 데스크톱 및 모바일 애플리케이션을 구축할 수 있는 강력한 그래픽 UI 툴킷입니다. 이 글에서는 최근 몇 년간 개발된 새로운 기능들을 소개하며, JavaFX 24의 출시와 함께 선보인 RichTextArea(인큐베이터), CSS 전환, 플랫폼 기본 설정 등의 기능을 설명합니다. 또한 다양한 데모와 샘플 코드도 제공됩니다. 마지막으로 앞으로 JavaFX에 추가될 기능들에 대한 미리보기도 제공합니다.
👉 [자세히 보기](https://inside.java/2025/05/10/javaone-javafx/)

## 🔹 Golang - More predictable benchmarking with testing.B.Loop
이 블로그 글은 Go 1.24에서 도입된 `testing.B.Loop` 기능을 소개합니다. 이 기능은 벤치마킹을 더욱 예측 가능하게 만들어주며, 더 나은 반복 실행을 통해 성능 테스트의 정확성을 향상시킵니다. 이를 통해 개발자들은 코드의 성능을 더 효율적으로 분석하고 최적화할 수 있습니다.
👉 [자세히 보기](https://go.dev/blog/testing-b-loop)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
제목: Helm @ KubeCon + CloudNativeCon EU '25

Helm 팀이 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU '25에 참가합니다. 올해 말 출시 예정인 Helm 4에 관한 논의에 참여할 수 있는 기회로, 발표 세션과 Project Pavilion의 Helm 부스에서 유지보수자들과 대화할 수 있습니다. 주간 동안 진행되는 모든 Helm 관련 활동에 대한 자세한 내용은 링크를 확인하세요.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

