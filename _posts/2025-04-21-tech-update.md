# 🛠️ 2025-04-21 기술 업데이트 요약

## 🔹 Kubernetes - Introducing kube-scheduler-simulator
제목: kube-scheduler-simulator 소개

요약: Kubernetes 스케줄러는 Pod가 실행될 노드를 결정하는 중요한 컨트롤 플레인 구성 요소입니다. kube-scheduler-simulator는 Kubernetes 스케줄러를 위한 시뮬레이터로, Google Summer of Code 2021 프로젝트로 시작되었습니다. 이 도구는 사용자가 스케줄러의 동작과 결정을 자세히 살펴볼 수 있도록 합니다. 스케줄링 제약 조건을 사용하는 일반 사용자와 맞춤형 플러그인으로 스케줄러를 확장하는 전문가 모두에게 유용합니다.

스케줄러의 행동을 이해하는 것은 많은 요인을 고려하기 때문에 어렵습니다. kube-scheduler-simulator는 이러한 문제를 해결하기 위해 설계되었습니다. 사용자는 스케줄링 제약 조건, 스케줄러 구성 및 맞춤형 플러그인을 테스트하고 모든 스케줄링 결정을 검토할 수 있습니다. 시뮬레이터는 스케줄러의 내부 결정을 노출하여 사용자가 스케줄러의 작동 방식을 이해하고 적절한 스케줄링 제약 조건을 정의할 수 있도록 돕습니다. 개발 환경에서뿐만 아니라 프로덕션 환경과 유사한 환경에서 새로운 스케줄러 버전을 테스트할 수 있는 기능도 제공합니다.

시뮬레이터는 Docker만 설치되어 있으면 실행할 수 있으며, Kubernetes 클러스터가 필요하지 않습니다. 더 자세한 정보는 kube-scheduler-simulator 저장소에서 확인할 수 있습니다. Kubernetes SIG Scheduling이 개발을 주도하고 있으며, 피드백과 기여를 환영합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/04/07/introducing-kube-scheduler-simulator/)

## 🔹 Spring Boot - A Bootiful Podcast: 'Mr. Apache' Jeff Genender
제목: 아름다운 팟캐스트: 'Mr. Apache' Jeff Genender

요약: 안녕하세요, Spring 팬 여러분! 이번 에피소드에서는 Java 커뮤니티의 잘 알려진 멤버인 Jeff Genender와 함께합니다. 그는 수십 년 동안 Apache에 기여하며 여러분이 익숙한 여러 주요 프로젝트를 추진해왔습니다.
👉 [자세히 보기](https://spring.io/blog/2025/04/17/a-bootiful-podcast-jeff-genender)

## 🔹 Docker - Docker Desktop for Mac: QEMU Virtualization Option to be Deprecated in 90 Days
제목: Docker Desktop for Mac: QEMU 가상화 옵션, 90일 후 폐기 예정

요약: Apple Silicon Mac용 Docker Desktop에서 가상화 옵션으로 사용되던 QEMU의 폐기를 발표합니다. Apple Silicon으로의 초기 전환 기간 동안 QEMU가 유산 가상화 솔루션으로 역할을 했지만, 이제 2025년 7월 14일을 기점으로 90일 후 완전히 폐기될 예정입니다. 이 폐기는 QEMU의 에뮬레이션 역할에는 영향을 미치지 않습니다.
👉 [자세히 보기](https://www.docker.com/blog/docker-desktop-for-mac-qemu-virtualization-option-to-be-deprecated-in-90-days/)

## 🔹 Java - Where Is the Java Language Going?
제목: 자바 언어는 어디로 향하고 있는가?

요약: 자바 언어 설계자인 브라이언 괴츠와 함께 최근의 개선 사항과 자바 언어의 미래 방향에 대해 알아보세요. 특히 프로젝트 앰버(Project Amber)와 프로젝트 발할라(Project Valhalla)에 중점을 두고 있습니다.
👉 [자세히 보기](https://inside.java/2025/04/20/javaone-future-java/)

## 🔹 Golang - More predictable benchmarking with testing.B.Loop
제목: testing.B.Loop를 사용한 더 예측 가능한 벤치마킹

요약: Go 1.24에서는 개선된 벤치마크 루프 기능을 제공합니다. 이 새로운 기능은 벤치마킹을 보다 예측 가능하게 만들어 개발자들이 코드의 성능을 더 정확하게 측정할 수 있도록 돕습니다.
👉 [자세히 보기](https://go.dev/blog/testing-b-loop)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
제목: Helm @ KubeCon + CloudNativeCon EU '25

요약: <p>올해도 어김없이 Helm 팀이 KubeCon + CloudNativeCon EU '25에 참석하기 위해 영국 런던으로 향합니다. 이번 행사는 4월 1일부터 4일까지 열립니다. Helm 4가 올해 말 출시될 예정이니, 토크 세션과 프로젝트 파빌리온의 Helm 부스에서 유지 관리자들과의 대화에 꼭 참여해 보세요. 이번 주 동안 진행될 모든 Helm 관련 활동의 자세한 내용은 아래를 참고하세요.</p>
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

