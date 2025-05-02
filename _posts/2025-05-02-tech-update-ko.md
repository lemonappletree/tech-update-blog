# 🛠️ 2025-05-02 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.33: New features in DRA
Kubernetes v1.33에서는 Dynamic Resource Allocation (DRA) 기능이 개선되었습니다. DRA는 v1.26에서 알파 기능으로 도입되었고, v1.31에서 큰 변화를 겪었습니다. v1.32에서는 베타로 승격되었으며, v1.34에서 일반적으로 사용 가능하게 될 예정입니다.

v1.33에서 DRA는 여전히 베타 상태이지만, 새로운 기능과 사용자 경험 개선이 추가되었습니다. 주요 업데이트로는 드라이버가 특정 장치의 상태를 보고할 수 있는 '드라이버 소유 리소스 클레임 상태'가 베타로 승격되었습니다. 새로운 알파 기능으로는 '분할 가능한 장치', '장치 오염 및 허용', '우선순위 목록', '관리자 액세스' 등이 추가되었습니다. 또한, 새로운 v1beta2 API가 추가되어 사용자 경험을 간소화하고 미래의 추가 기능 도입을 준비하고 있습니다.

v1.34에서는 DRA의 일반 가용성을 목표로 하고 있으며, 알파 기능들은 베타로 승격될 예정입니다. DRA 개발에 참여하고 싶다면, Kubernetes 장치 관리 작업 그룹의 Slack 채널과 회의에 참여할 수 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/05/01/kubernetes-v1-33-dra-updates/)

## 🔹 Spring Boot - A Bootiful Podcast: Spring instructor Mary Ellen Bowman
블로그 글 요약: 이번 에피소드에서는 전설적인 스프링 강사인 메리 엘렌 보우먼과의 인터뷰를 소개합니다. 스프링 팬이라면 놓치지 말아야 할 흥미로운 대화가 담겨 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/05/01/a-bootiful-podcast-mary-ellen-bowman)

## 🔹 Docker - Update on the Docker DX extension for VS Code
제목: VS Code용 Docker DX 확장 업데이트

요약: Visual Studio Code용 새로운 Docker DX 확장이 출시된 지 몇 주가 지났습니다. 이 출시는 컨테이너화된 애플리케이션을 개발하는 개발자를 더 잘 지원하기 위한 Docker와 Microsoft 간의 깊은 협력을 반영합니다. 지난 몇 주 동안 VS Code의 Docker 확장에서 몇 가지 변화를 눈치챘을 수 있습니다.
👉 [자세히 보기](https://www.docker.com/blog/docker-dx-extension-for-vs-code-update/)

## 🔹 Java - Strings Just Got Faster
JDK 25에서는 불변 맵에서 키로 사용되는 문자열의 성능이 크게 향상되었습니다. 이로 인해 맵 작업이 더 빠르고 효율적으로 수행될 수 있습니다.
👉 [자세히 보기](https://inside.java/2025/05/01/strings-just-got-faster/)

## 🔹 Golang - More predictable benchmarking with testing.B.Loop
Go 1.24 버전에서는 `testing.B.Loop` 기능을 도입하여 벤치마크 루프의 예측 가능성을 개선했습니다. 이 기능은 벤치마크 테스트에서 반복 실행의 일관성을 높여 더 정확한 성능 측정을 가능하게 합니다. 자세한 내용은 Go 블로그의 해당 페이지에서 확인할 수 있습니다.
👉 [자세히 보기](https://go.dev/blog/testing-b-loop)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
제목: Helm @ KubeCon + CloudNativeCon EU '25

Helm 팀이 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU '25에 참가합니다. 올해 말 출시 예정인 Helm 4에 대한 논의를 위해 유지 관리자들과의 대화에 참여하고, Project Pavilion의 Helm 부스도 방문해 보세요. 주간 동안 진행되는 모든 Helm 관련 활동에 대한 자세한 내용은 링크를 참조하세요.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

