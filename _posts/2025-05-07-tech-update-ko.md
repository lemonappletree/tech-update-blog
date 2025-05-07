# 🛠️ 2025-05-07 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.33: Fine-grained SupplementalGroups Control Graduates to Beta
이 블로그 글은 Kubernetes v1.33에서 `supplementalGroupsPolicy` 기능이 베타 버전으로 승격되었음을 설명합니다. 이 기능은 컨테이너에서 보조 그룹에 대한 더 정밀한 제어를 가능하게 하여 보안 상태를 강화하고, 특히 볼륨 접근 시 보안을 개선할 수 있습니다. 또한 컨테이너 내 UID/GID 세부사항의 투명성을 높여 보안 감시를 향상시킵니다. 이 베타 버전에서는 일부 행동 변화가 있으며, 업그레이드 시 고려 사항을 참고해야 합니다. `supplementalGroupsPolicy`는 `Merge`와 `Strict` 두 가지 정책을 제공하며, `Strict` 정책은 컨테이너 이미지의 `/etc/group`에 정의된 그룹을 무시합니다. 이를 통해 예상치 못한 접근 제어 문제를 방지할 수 있습니다. 이 기능은 최신 CRI 버전이 필요하며, Kubernetes 커뮤니티에 참여하여 추가 정보를 얻을 수 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/05/06/kubernetes-v1-33-fine-grained-supplementalgroups-control-beta/)

## 🔹 Spring Boot - This Week in Spring - May 6th, 2025
이번 주 Spring 블로그 글의 요약은 다음과 같습니다:

이번 주 필자는 Devoxx UK 이벤트 참석을 위해 런던을 방문 중이며, 이후 마이애미의 Code Remix와 탬파 JUG에서 발표를 진행할 예정입니다. 또한 스톡홀름의 JForum 이벤트에도 참석하여 Spring에 대한 심층적인 논의를 할 계획입니다. 5월 20일에는 Spring AI가 출시되고, Spring Boot 3.5도 그 후에 발표될 예정입니다. Spring I/O에서는 Rod Johnson과 Juergen Hoeller와 함께 특별한 발표를 진행하며, GraalVM 창시자 Thomas Wuerthinger와도 발표가 예정되어 있습니다.

이번 주에는 다양한 업데이트가 있습니다:
- Spring AI의 Model Context Protocol에 대한 동적 도구 업데이트
- Spring Cloud 2025.0.0-RC1, Spring AI 1.0.0-M8의 출시
- Spring Boot 애플리케이션 구축 튜토리얼
- Spring AI 관련 평가 테스트의 중요성
- JDK 25에서 인스턴스 메인 메서드가 미리보기에서 최종으로 이동

보다 자세한 내용은 Spring 블로그에서 확인할 수 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/05/06/this-week-in-spring-may-6th-2025)

## 🔹 Docker - Securing Model Context Protocol: Safer Agentic AI with Containers
블로그 글은 "모델 컨텍스트 프로토콜(MCP)" 도구의 보안 문제에 대해 다루고 있습니다. MCP 도구의 채택이 가속화됨에 따라 보안 관련 우려도 증가하고 있습니다. MCP 도구는 에이전트의 자율성을 높여 사용자 기대와 에이전트 행동 간의 불일치 및 통제되지 않은 실행과 관련된 새로운 위험을 초래할 수 있습니다. 이러한 시스템은 새로운 보안 과제를 제시합니다.
👉 [자세히 보기](https://www.docker.com/blog/whats-next-for-mcp-security/)

## 🔹 Java - JEP targeted to JDK 25: 512: Compact Source Files and Instance Main Methods
블로그 글은 JDK 25에 목표로 한 JEP 512에 관한 내용입니다. 이 JEP는 'Compact Source Files'와 'Instance Main Methods'라는 두 가지 주요 기능을 소개합니다. 자세한 내용은 제공된 링크를 통해 확인할 수 있습니다.
👉 [자세히 보기](https://inside.java/2025/05/06/jep512-target-jdk25/)

## 🔹 Golang - More predictable benchmarking with testing.B.Loop
제목: 테스트.B.Loop을 통한 더 예측 가능한 벤치마킹  
요약: Go 1.24 버전에서는 벤치마크 루프 기능이 향상되었습니다. 이를 통해 개발자들은 보다 예측 가능한 방식으로 벤치마킹을 수행할 수 있습니다.  
링크: [Go 블로그](https://go.dev/blog/testing-b-loop)
👉 [자세히 보기](https://go.dev/blog/testing-b-loop)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
제목: Helm @ KubeCon + CloudNativeCon EU '25

요약: Helm 팀이 2025년 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU에 참가합니다. 올해 말 출시 예정인 Helm 4에 대한 논의에 참여할 수 있는 기회가 제공되며, 유지관리자들과의 대화 세션 및 Project Pavilion에 있는 Helm 부스를 방문할 수 있습니다. 주간 동안 진행되는 모든 Helm 관련 활동에 대한 자세한 내용은 링크를 참조하세요.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

