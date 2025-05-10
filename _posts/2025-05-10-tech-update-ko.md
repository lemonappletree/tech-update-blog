# 🛠️ 2025-05-10 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.33: Streaming List responses
이 블로그 글은 Kubernetes v1.33의 새로운 기능인 "스트리밍 인코딩"을 소개합니다. 이 기능은 대규모 클러스터에서 대량의 데이터를 요청하는 List 요청을 처리할 때 발생하는 불필요한 메모리 사용 문제를 해결합니다. 기존 방식은 응답 데이터를 한 번에 메모리에 저장하고 전송했지만, 새로운 스트리밍 인코딩은 데이터를 아이템 단위로 개별 처리하여 메모리 사용을 줄입니다. 이를 통해 API 서버의 메모리 사용량을 크게 줄이고, 클러스터의 안정성과 성능을 향상시킵니다. 벤치마크 결과, 이 개선을 통해 메모리 사용량이 70-80GB에서 3GB로 감소했습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/05/09/kubernetes-v1-33-streaming-list-responses/)

## 🔹 Spring Boot - A Bootiful Podcast: V Körbes on security from the platform on up
블로그 글 요약: 이번 특별한 팟캐스트에서는 Broadcom의 V Körbes와 함께 애플리케이션 위와 아래에서의 보안에 대해 이야기합니다.
👉 [자세히 보기](https://spring.io/blog/2025/05/08/a-bootiful-podcast-v-korbes)

## 🔹 Docker - Securing Model Context Protocol: Safer Agentic AI with Containers
기술 블로그 글의 제목은 "모델 컨텍스트 프로토콜 보안: 컨테이너로 더 안전해진 에이전틱 AI"입니다. 요약하자면, 모델 컨텍스트 프로토콜(MCP) 도구는 주로 초기 사용자들에 의해 사용되고 있지만, 더 넓은 범위로의 채택이 가속화되고 있습니다. 이러한 성장과 함께 MCP 보안 문제도 점점 더 중요해지고 있습니다. 에이전트 자율성을 높임으로써, MCP 도구는 사용자 기대와 에이전트 행동 간의 불일치 및 통제되지 않은 실행과 관련된 새로운 위험을 초래합니다. 이러한 시스템은 또한 새로운 보안 문제를 제기하고 있습니다.
👉 [자세히 보기](https://www.docker.com/blog/whats-next-for-mcp-security/)

## 🔹 Java - Structured Concurrency Revamp in Java 25 - Inside Java Newscast #91
Java 25의 구조적 동시성 개선에 대한 블로그 글은 JDK 개선 제안서 505를 통해 JDK 25에서 구조적 동시성 API를 개편한 내용을 다루고 있습니다. 주요 변경 사항으로는 구성 옵션과 조인 기능의 도입이 포함됩니다.
👉 [자세히 보기](https://inside.java/2025/05/08/newscast-91/)

## 🔹 Golang - More predictable benchmarking with testing.B.Loop
이 기술 블로그 글에서는 Go 1.24 버전에서 도입된 `testing.B.Loop` 기능을 통해 벤치마킹의 예측 가능성을 개선하는 방법을 다루고 있습니다. `testing.B.Loop`는 기존의 벤치마크 루프 방식을 개선하여 더 안정적이고 일관된 결과를 제공하도록 설계되었습니다. 이를 통해 개발자들은 벤치마크 테스트를 더 효과적으로 수행할 수 있게 됩니다.
👉 [자세히 보기](https://go.dev/blog/testing-b-loop)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
블로그 글 요약: Helm 팀이 2025년 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU '25에 참가합니다. 올해 후반에 출시될 Helm 4에 대한 논의가 진행 중이니, 발표 세션과 Helm 부스를 방문하여 유지 관리자들과 대화에 참여하세요. 행사 주간 동안의 모든 Helm 관련 활동에 대한 자세한 내용은 블로그 글을 참고하세요.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

