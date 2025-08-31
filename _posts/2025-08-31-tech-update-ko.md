# 🛠️ 2025-08-31 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.34: Finer-Grained Control Over Container Restarts
Kubernetes 1.34 버전에는 새로운 알파 기능인 'Container Restart Policy and Rules'가 도입되어, Pod의 전역 재시작 정책을 개별 컨테이너 수준에서 오버라이드할 수 있게 되었습니다. 이 기능을 통해 각 컨테이너의 재시작 정책을 별도로 지정할 수 있으며, 종료 코드에 따라 조건부로 컨테이너를 재시작할 수도 있습니다. 이 기능은 'ContainerRestartRules'라는 알파 기능 게이트 뒤에 숨겨져 있습니다. 이전까지는 Pod 수준에서 재시작 정책이 설정되어, 모든 컨테이너가 동일한 재시작 정책을 공유해야 했으나, 이번 업데이트로 인해 복잡한 시나리오를 보다 세밀하게 관리할 수 있게 되었습니다. 예를 들어, AI/ML 트레이닝 작업에서 실패한 컨테이너를 신속하게 "인플레이스"로 재시작할 수 있으며, 초기화 컨테이너를 한 번만 시도하게 할 수도 있습니다. 새로운 기능을 사용하려면 Kubernetes 클러스터에서 해당 기능 게이트를 활성화해야 하며, 이후 컨테이너 정의에서 'restartPolicy'와 'restartPolicyRules'를 지정할 수 있습니다. 앞으로 더 많은 Pod 및 컨테이너 재시작 관련 기능이 추가될 예정이며, 커뮤니티의 피드백을 환영합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/08/29/kubernetes-v1-34-per-container-restart-policy/)

## 🔹 Spring Boot - A Bootiful Podcast: JobRunr founder Ronald Dehuysser on what's new in version 8
제목: 아름다운 팟캐스트: JobRunr 창립자 Ronald Dehuysser가 전하는 버전 8의 새로운 점

요약: Spring 팬 여러분, 안녕하세요! 이번 에피소드에서는 흥미롭고 피곤했던 SpringOne 2025 행사 직후, JobRunr 창립자인 Ronald Dehuysser와 함께 JobRunr 버전 8.0.0의 새로운 기능에 대해 이야기하게 되어 기쁩니다. JobRunr v8에 대한 더 많은 정보를 알고 싶다면 [여기](https://www.jobrunr.io/en/blog/v8-release/)를 방문하세요!
👉 [자세히 보기](https://spring.io/blog/2025/08/28/a-bootiful-podcast-ronald-dehuysser)

## 🔹 Docker - Broadcom’s New Bitnami Restrictions? Migrate Easily with Docker
이 블로그 글에서는 Broadcom의 새로운 Bitnami 사용 제한에 대해 다루고 있습니다. Bitnami는 오픈 소스 및 클라우드 네이티브 커뮤니티에서 중요한 역할을 하여 개발자와 운영자가 인기 있는 애플리케이션을 신뢰할 수 있는 사전 제작된 컨테이너 이미지와 Helm 차트를 사용하여 쉽게 배포할 수 있도록 도와왔습니다. 많은 팀이 WordPress부터 PostgreSQL까지 다양한 애플리케이션의 설치 및 업데이트 표준화에서 혜택을 받아왔습니다. 이러한 변화에 대응하여 Docker를 사용하여 쉽게 마이그레이션하는 방법을 소개하고 있습니다.
👉 [자세히 보기](https://www.docker.com/blog/broadcoms-new-bitnami-restrictions-migrate-easily-with-docker/)

## 🔹 Java - The Java Platform Extension is now also available on open-vsx.org
블로그 글 요약: VS Code용 새로운 Java 플랫폼 확장이 이제 open-vsx.org에서도 이용 가능하게 되었습니다. 이 업데이트는 Java 개발자들에게 더 많은 선택권과 유연성을 제공하며, VS Code 환경에서 Java 개발을 더욱 편리하게 합니다.
👉 [자세히 보기](https://inside.java/2025/08/29/java-vscode-extension-update/)

## 🔹 Golang - Testing Time (and other asynchronicities)
"Testing Time (and other asynchronicities)" 블로그 글은 비동기 코드를 테스트하는 방법에 대해 논의하고 있으며, `testing/synctest` 패키지를 탐구합니다. 이 내용은 GopherCon Europe 2025에서 같은 제목으로 발표된 강연을 기반으로 하고 있습니다.
👉 [자세히 보기](https://go.dev/blog/testing-time)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
제목: Helm @ KubeCon + CloudNativeCon EU '25  
요약: Helm 팀이 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU '25에 참석합니다. 올해 말 출시 예정인 Helm 4에 대한 논의를 위해, 발표 세션과 프로젝트 파빌리온의 Helm 부스에서 유지 관리자들과 대화에 참여해 보세요. 주간 동안 진행되는 모든 Helm 관련 활동에 대한 자세한 내용은 아래 링크를 통해 확인할 수 있습니다.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

