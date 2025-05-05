# 🛠️ 2025-05-05 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.33: Mutable CSI Node Allocatable Count
이 기술 블로그 글은 Kubernetes v1.33에 도입된 알파 기능인 '변경 가능한 CSI 노드 할당 가능 수'에 대해 설명하고 있습니다. 이 기능은 CSI 드라이버가 노드가 처리할 수 있는 최대 볼륨 수를 동적으로 업데이트할 수 있도록 하여, 포드 스케줄링 결정의 정확성을 높이고, 오래된 볼륨 용량 정보로 인한 스케줄링 오류를 줄입니다. 전통적으로는 고정된 볼륨 첨부 한도를 보고했지만, 이 기능을 통해 주기적 및 반응적 업데이트가 가능해져, 스케줄러가 최신 노드 용량 정보를 확보할 수 있게 됩니다. 이를 위해 `kube-apiserver`와 `kubelet` 구성 요소에서 이 기능 게이트를 활성화해야 하며, CSI 드라이버 설정에서 업데이트 주기를 지정할 수 있습니다. 이 기능은 현재 알파 단계이며, 커뮤니티의 피드백을 통해 지속적으로 발전할 예정입니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/05/02/kubernetes-1-33-mutable-csi-node-allocatable-count/)

## 🔹 Spring Boot - Dynamic Tool Updates in Spring AI's Model Context Protocol
이 기술 블로그는 Spring AI의 Model Context Protocol(MCP)에서 동적 도구 업데이트 기능에 대해 설명합니다. MCP는 AI 모델이 외부 도구와 자원에 표준화된 인터페이스를 통해 접근할 수 있도록 해주는 강력한 기능입니다. 이 블로그는 Spring AI가 MCP에서 동적 도구 업데이트를 구현하여 AI 기반 애플리케이션에 유연성과 확장성을 제공하는 방법을 탐구합니다. MCP의 서버와 클라이언트는 런타임에 도구를 추가하거나 제거할 수 있으며, 이러한 변경 사항은 AI 모델이 즉시 인식하고 사용할 수 있습니다. 이 기능은 AI 애플리케이션이 런타임 조건과 사용자 요구에 따라 그 기능을 확장할 수 있도록 해줍니다. 예제 코드는 GitHub에서 확인할 수 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/05/04/spring-ai-dynamic-tool-updates-with-mcp)

## 🔹 Docker - Update on the Docker DX extension for VS Code
제목: VS Code용 Docker DX 확장 업데이트  
요약: 몇 주 전, Visual Studio Code를 위한 새로운 Docker DX 확장이 출시되었습니다. 이번 출시는 컨테이너화된 애플리케이션을 개발하는 개발자들을 더 잘 지원하기 위한 Docker와 Microsoft 간의 긴밀한 협력을 반영합니다. 지난 몇 주 동안 VS Code의 Docker 확장에서 몇 가지 변화가 있었음을 알 수 있을 것입니다.
👉 [자세히 보기](https://www.docker.com/blog/docker-dx-extension-for-vs-code-update/)

## 🔹 Java - Java for AI
블로그 글 "Java for AI"는 Java의 다양한 기능이 AI의 요구를 충족할 수 있음을 설명합니다. 기존 기능으로는 Foreign Function and Memory API와 Vector API가 있으며, 향후 기능으로는 Project Valhalla와 Project Babylon에서 제안된 것들이 포함됩니다. 이 비디오는 이러한 기능들이 Java 라이브러리와 애플리케이션에서 어떻게 사용되어 경쟁력 있는 AI 솔루션을 구축할 수 있는지를 논의합니다.
👉 [자세히 보기](https://inside.java/2025/05/03/javaone-java-ai/)

## 🔹 Golang - More predictable benchmarking with testing.B.Loop
해당 기술 블로그 글은 Go 1.24에서 개선된 벤치마크 루프 기능에 대해 설명합니다. 새로운 `testing.B.Loop` 기능을 통해 벤치마크 테스트가 더 예측 가능하게 수행되며, 코드 성능 측정의 정확성이 향상됩니다. 이를 통해 개발자들은 Go 언어를 사용할 때 더 효율적으로 코드를 최적화할 수 있게 됩니다.
👉 [자세히 보기](https://go.dev/blog/testing-b-loop)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
제목: Helm @ KubeCon + CloudNativeCon EU '25

Helm 팀이 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU '25에 참석합니다. 올해 말 출시 예정인 Helm 4에 대해 논의할 수 있는 기회가 마련되어 있으며, 프로젝트 파빌리온의 Helm 부스에서 팀원들과 대화를 나눌 수 있습니다. 행사 기간 동안 진행되는 모든 Helm 관련 활동에 대한 자세한 내용은 링크를 통해 확인할 수 있습니다.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

