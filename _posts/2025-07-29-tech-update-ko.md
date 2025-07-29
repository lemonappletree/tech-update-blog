# 🛠️ 2025-07-29 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.34 Sneak Peek
블로그 글 요약: Kubernetes v1.34 버전이 2025년 8월 말에 출시될 예정입니다. 이번 릴리스에는 제거나 폐기되는 기능이 없지만, 여러 가지 개선 사항이 포함되어 있습니다. 주요 기능으로는 안정적인 상태로 졸업을 목표로 하는 동적 자원 할당(DRA), 이미지 풀 인증을 위한 ServiceAccount 토큰, 배포 시 Pod 교체 정책, kubelet 및 API 서버를 위한 생산 준비 완료 추적, 같은 영역 및 노드 트래픽 분배 기능, KYAML 지원, HPA의 세밀한 자동 확장 제어 기능이 있습니다. 각 기능은 아직 개발 중이며, 릴리스 전 변경될 수 있습니다. Kubernetes 커뮤니티에 참여하거나 더 많은 정보를 얻고 싶다면 여러 채널을 통해 커뮤니티에 참여할 수 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/07/28/kubernetes-v1-34-sneak-peek/)

## 🔹 Spring Boot - Spring Modulith 2.0 M1 released
Spring Modulith 2.0 M1이 출시되었습니다. 이번 릴리스는 Spring Boot 4 M1과 Spring Framework 7.0 M7을 기반으로 하며, 주요 특징은 새롭게 개편된 이벤트 발행 레지스트리입니다. 이는 기존 버전의 한계를 해결하고, 새로운 상태 모델을 도입하여 이벤트 발행 상태를 보다 명확하게 구분할 수 있게 합니다. 또한, 다중 인스턴스 애플리케이션 배포를 지원하면서도 분산 잠금을 필요로 하지 않습니다. JDBC 구현도 이 새로운 모델을 지원하도록 조정되었습니다. 기존 애플리케이션은 여전히 기존 상태 전환을 유지하며 작동할 수 있습니다. 새로운 레지스트리에 대한 세부 사항과 마이그레이션 방법이 제공되며, 피드백을 환영합니다. 전체 변경 로그는 GitHub에서 확인할 수 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/07/26/spring-modulith-2-0-M1-released)

## 🔹 Docker - Beyond the Chatbot: Event-Driven Agents in Action
Docker는 최근 내부 24시간 해커톤을 개최하여 "생산성을 높이는 에이전트 만들기"라는 간단한 목표를 설정했습니다. 작성자는 채팅 인터페이스에서 시간을 더 소비하지 않고, 인간의 개입 없이 완전히 자동화된 에이전트를 만들고 싶다고 생각했습니다.
👉 [자세히 보기](https://www.docker.com/blog/beyond-the-chatbot-event-driven-agents-in-action/)

## 🔹 Java - Episode 39 “Deprecations &amp; Removals” with Stuart Marks
제목: 에피소드 39 "Deprecations & Removals" with Stuart Marks

요약: Java는 새로운 기능을 추가하는 것뿐만 아니라, 유지 보수에 부담이 되거나 성능에 악영향을 미치거나 사용에 위험이 있는 오래된 기능들을 제거하고 있습니다. 이번 에피소드에서는 32비트 포트, 애플릿, 종료(finalization), 보안 관리자(security manager)에 대해 다룹니다.
👉 [자세히 보기](https://inside.java/2025/07/28/podcast-039/)

## 🔹 Golang - The FIPS 140-3 Go Cryptographic Module
제목: FIPS 140-3 Go 암호화 모듈  
요약: Go 언어에 FIPS 140-3 표준을 준수하는 모드가 기본적으로 내장되었습니다.  
링크: https://go.dev/blog/fips140  

이 블로그 글에서는 Go 언어가 이제 FIPS 140-3 표준을 준수하는 암호화 모드를 제공한다는 내용을 다루고 있습니다. 이는 보안 요구 사항을 충족하기 위해 중요한 발전이며, 사용자는 Go 내에서 직접 해당 모드를 활용할 수 있게 됩니다.
👉 [자세히 보기](https://go.dev/blog/fips140)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
블로그 글 요약: Helm 팀이 2025년 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU '25에 참가합니다. 올해 말 출시 예정인 Helm 4에 관한 논의를 위해 팀의 발표 세션과 Project Pavilion의 Helm 부스를 방문해 주세요. 행사 동안 진행되는 모든 Helm 관련 활동에 대한 자세한 내용은 링크를 참조하세요.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

