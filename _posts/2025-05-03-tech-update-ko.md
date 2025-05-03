# 🛠️ 2025-05-03 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.33: Mutable CSI Node Allocatable Count
Kubernetes v1.33에서는 상태 저장 애플리케이션의 신뢰할 수 있는 스케줄링을 위해 '변경 가능한 CSI 노드 할당 가능 수량'이라는 알파 기능을 도입했습니다. 이 기능은 CSI 드라이버가 노드가 처리할 수 있는 최대 볼륨 수를 동적으로 업데이트할 수 있도록 하여, 보다 정확한 스케줄링 결정을 내리고 오래된 볼륨 용량 정보로 인한 스케줄링 실패를 줄입니다. 전통적으로 Kubernetes CSI 드라이버는 초기화 시 고정된 최대 볼륨 첨부 제한을 보고했지만, 실제 첨부 용량은 노드의 생애 주기 동안 다양한 이유로 변경될 수 있습니다. 이 새로운 기능은 Kubernetes가 실행 중에 노드 첨부 용량을 동적으로 조정하고 보고할 수 있게 하여, 스케줄러가 가장 정확하고 최신의 노드 용량 정보를 가질 수 있도록 합니다. 이를 위해 'kube-apiserver'와 'kubelet' 컴포넌트에서 이 기능을 활성화해야 하며, CSI 드라이버 설정에서 주기적인 업데이트를 구성할 수 있습니다. 이 기능은 현재 알파 상태이며, 커뮤니티는 사용자의 피드백을 환영합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/05/02/kubernetes-1-33-mutable-csi-node-allocatable-count/)

## 🔹 Spring Boot - A Bootiful Podcast: Spring instructor Mary Ellen Bowman
블로그 글 요약: 이 글에서는 유명한 스프링 강사인 Mary Ellen Bowman과의 팟캐스트 인터뷰가 소개됩니다. 스프링 팬들에게 흥미로운 대화를 제공합니다.
👉 [자세히 보기](https://spring.io/blog/2025/05/01/a-bootiful-podcast-mary-ellen-bowman)

## 🔹 Docker - Update on the Docker DX extension for VS Code
이 블로그 글은 Visual Studio Code를 위한 새로운 Docker DX 확장 프로그램 출시 후 몇 주가 지난 현재의 상황을 다루고 있습니다. 이번 출시는 Docker와 Microsoft 간의 협력을 강화하여 컨테이너화된 애플리케이션을 개발하는 개발자들을 더 잘 지원하기 위한 것입니다. 최근 몇 주 동안 VS Code의 Docker 확장에서 몇 가지 변화를 경험했을 수 있습니다.
👉 [자세히 보기](https://www.docker.com/blog/docker-dx-extension-for-vs-code-update/)

## 🔹 Java - JEP targeted to JDK 25: 511: Module Import Declarations
이 기술 블로그 글은 JDK 25에 목표를 둔 JEP 511에 관한 내용입니다. JEP 511은 모듈 임포트 선언에 대한 내용을 다루고 있습니다. 해당 JEP의 자세한 내용은 링크를 통해 확인할 수 있습니다.
👉 [자세히 보기](https://inside.java/2025/05/02/jep511-target-jdk25/)

## 🔹 Golang - More predictable benchmarking with testing.B.Loop
이 기술 블로그 글은 Go 1.24 버전에서 개선된 벤치마크 루핑 기능인 `testing.B.Loop`에 대해 설명합니다. 새로운 기능을 통해 더 예측 가능한 벤치마킹이 가능해졌으며, 이를 통해 개발자들은 성능 테스트를 더욱 효율적으로 수행할 수 있습니다.
👉 [자세히 보기](https://go.dev/blog/testing-b-loop)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
블로그 글 요약: Helm 팀이 2025년 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU에 참석합니다. 올해 말 출시 예정인 Helm 4에 대한 논의에 참여하려면, 발표 세션과 Helm 부스를 방문하세요. 행사 주간 동안 Helm 관련 활동에 대한 자세한 내용은 링크를 통해 확인할 수 있습니다.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

