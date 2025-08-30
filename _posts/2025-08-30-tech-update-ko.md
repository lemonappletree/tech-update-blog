# 🛠️ 2025-08-30 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.34: Finer-Grained Control Over Container Restarts
Kubernetes 1.34 버전에서는 컨테이너 재시작을 더 세밀하게 제어할 수 있는 새로운 알파 기능이 도입되었습니다. 이 기능은 각 컨테이너에 개별적인 재시작 정책을 설정할 수 있게 해주며, Pod의 전역 재시작 정책을 무시할 수 있습니다. 또한, 종료 코드에 따라 조건부로 개별 컨테이너를 재시작할 수 있습니다. 이 기능은 `ContainerRestartRules`라는 알파 기능 게이트를 통해 사용 가능합니다.

이전에는 Pod 단위로 재시작 정책이 설정되었기 때문에 모든 컨테이너가 동일한 재시작 정책을 공유해야 했습니다. 이는 일부 사용 사례에서 제한적이었습니다. 하지만 이번 기능을 통해 각 컨테이너에 맞는 재시작 정책을 지정할 수 있어 더 복잡한 시나리오를 처리할 수 있습니다.

주요 사용 사례로는 AI/ML 연구의 장기 실행 작업에서의 "인-플레이스" 재시작, 한 번만 실행되는 초기화 컨테이너, 여러 컨테이너가 포함된 Pod 각각에 다른 재시작 요구사항 적용 등이 있습니다.

새로운 기능을 사용하기 위해 Kubernetes 1.34+ 버전의 클러스터에서 `ContainerRestartRules` 기능 게이트를 활성화해야 하며, 컨테이너 정의에서 `restartPolicy` 및 `restartPolicyRules` 필드를 지정해야 합니다. 이 기능에 대한 피드백은 Kubernetes SIG Node 커뮤니티를 통해 공유할 수 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/08/29/kubernetes-v1-34-per-container-restart-policy/)

## 🔹 Spring Boot - A Bootiful Podcast: JobRunr founder Ronald Dehuysser on what's new in version 8
제목: A Bootiful Podcast: JobRunr 창립자 Ronald Dehuysser가 전하는 버전 8의 새로운 기능

요약: Spring 팬 여러분, 안녕하세요! 이번 에피소드에서는 흥미롭고도 고된 SpringOne 2025 행사 직후, JobRunr의 창립자 Ronald Dehuysser와 함께 버전 8.0.0의 새로운 기능에 대해 이야기했습니다. JobRunr v8에 대한 자세한 내용은 [여기](https://www.jobrunr.io/en/blog/v8-release/)에서 확인하세요!
👉 [자세히 보기](https://spring.io/blog/2025/08/28/a-bootiful-podcast-ronald-dehuysser)

## 🔹 Docker - Boost Your Copilot with SonarQube via Docker MCP Toolkit and Gateway
이 블로그 글은 AI 코파일럿과 코드 생성 도구가 생산성을 크게 높여주지만, 보안에 취약하거나 테스트되지 않은 코드가 프로덕션에 들어갈 위험도 증가한다고 설명합니다. 이러한 문제를 해결하기 위한 도구로 SonarQube가 널리 사용되고 있으며, 이 도구는 코드의 취약점, 버그, 나쁜 관행을 방지하는 데 도움을 줍니다. Docker MCP Toolkit과 Gateway를 통해 SonarQube를 활용하여 코파일럿의 성능을 향상시키는 방법에 대해 다루고 있습니다.
👉 [자세히 보기](https://www.docker.com/blog/blog-sonarqube-copilot-docker-mcp-toolkit/)

## 🔹 Java - The Java Platform Extension is now also available on open-vsx.org
블로그 글 요약: 새로운 자바 플랫폼 확장이 VS Code용으로 출시되었으며, 이제 open-vsx.org에서도 사용할 수 있게 되었습니다. 이를 통해 개발자들은 더 다양한 플랫폼에서 자바 확장을 활용할 수 있게 되었습니다.
👉 [자세히 보기](https://inside.java/2025/08/29/java-vscode-extension-update/)

## 🔹 Golang - Testing Time (and other asynchronicities)
이 블로그 글은 비동기 코드 테스트와 `testing/synctest` 패키지에 대한 내용을 다루고 있습니다. 이 글은 GopherCon Europe 2025에서 발표된 같은 제목의 강연을 바탕으로 작성되었습니다. 비동기 코드의 테스트 방법과 관련 패키지의 활용에 대해 탐구합니다.
👉 [자세히 보기](https://go.dev/blog/testing-time)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
블로그 글 요약: Helm 팀이 2025년 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU에 참석합니다. 올해 말 출시 예정인 Helm 4에 대한 논의가 진행될 예정이며, 프로젝트 파빌리온의 Helm 부스와 발표 세션에서 유지관리자들과의 대화에 참여할 수 있습니다. 주간 동안의 Helm 관련 활동에 대한 자세한 정보는 제공된 링크에서 확인할 수 있습니다.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

