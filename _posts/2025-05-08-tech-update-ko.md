# 🛠️ 2025-05-08 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.33: From Secrets to Service Accounts: Kubernetes Image Pulls Evolved
이 기술 블로그 글은 Kubernetes의 최신 버전 v1.33에서 이미지 풀 인증 방식을 개선한 내용을 다룹니다. 기존에는 API에 저장된 장기 토큰이나 노드 수준에서 사용되는 자격 증명 제공자를 사용하여 이미지 풀을 인증했지만, 이는 보안과 운영상의 문제를 야기했습니다. 이를 해결하기 위해 Kubernetes는 Kubelet 자격 증명 제공자와의 서비스 계정 토큰 통합을 도입했습니다. 이 기능은 짧은 수명의 서비스 계정 토큰을 사용하여 특정 워크로드에 대한 인증을 제공함으로써 보안성을 높이고, 장기 이미지 풀 시크릿을 제거하여 관리의 복잡성을 줄입니다. 이 새로운 기능은 알파 버전으로 제공되며, 향후 릴리스에서 성능 개선과 더 많은 유연성을 제공할 계획입니다. 사용자는 Kubernetes 문서를 통해 더 많은 정보를 얻고, 기능을 직접 시도해볼 수 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/05/07/kubernetes-v1-33-wi-for-image-pulls/)

## 🔹 Spring Boot - This Week in Spring - May 6th, 2025
이번 주 Spring 블로그 글에서는 저자가 런던의 Devoxx UK 행사에 참석하기 위해 이동 중이라고 소개합니다. 이후에는 마이애미의 Code Remix와 탬파 JUG에서 발표를 하고, 스톡홀름의 JForum에서 Spring 관련 심도 있는 발표를 할 예정입니다. 가장 기대되는 소식으로는 5월 20일에 출시되는 Spring AI와 바로 며칠 뒤에 출시되는 Spring Boot 3.5가 있습니다. 바르셀로나에서 열리는 Spring I/O에서도 발표가 예정되어 있으며, Rod Johnson과 Juergen Hoeller와 함께 특별한 발표를 준비 중입니다. 또한 GraalVM 창립자 Thomas Wuerthinger와도 협업할 예정입니다. 여러 새로운 소식과 업데이트가 담긴 이번 블로그 글에서는 Spring AI의 모델 컨텍스트 프로토콜, 새로운 팟캐스트 에피소드, Spring Cloud 및 Spring AI 업데이트, 그리고 JDK 25 관련 소식 등을 소개합니다.
👉 [자세히 보기](https://spring.io/blog/2025/05/06/this-week-in-spring-may-6th-2025)

## 🔹 Docker - Securing Model Context Protocol: Safer Agentic AI with Containers
기술 블로그 글은 "모델 컨텍스트 프로토콜(MCP)" 도구의 보안 문제에 대해 다루고 있습니다. MCP 도구는 초기 사용자들에게 주로 사용되고 있지만, 점점 더 널리 채택되고 있습니다. 이러한 성장과 함께 MCP 보안 문제가 더욱 긴급해지고 있습니다. MCP 도구는 에이전트의 자율성을 높임으로써, 에이전트의 행동과 사용자 기대 사이의 불일치 및 통제되지 않은 실행과 관련된 새로운 위험을 초래합니다. 이러한 시스템은 또한 새로운 보안 문제를 제공합니다.
👉 [자세히 보기](https://www.docker.com/blog/whats-next-for-mcp-security/)

## 🔹 Java - JEP targeted to JDK 25: 512: Compact Source Files and Instance Main Methods
이 기술 블로그 글은 JDK 25에 목표로 하는 JEP 512에 대해 다루고 있습니다. 이 JEP는 소스 파일의 간소화 및 인스턴스 메인 메소드에 관한 내용을 포함하고 있습니다.
👉 [자세히 보기](https://inside.java/2025/05/06/jep512-target-jdk25/)

## 🔹 Golang - More predictable benchmarking with testing.B.Loop
이 블로그 글은 Go 1.24에서 개선된 벤치마크 루프 기능인 `testing.B.Loop`에 대해 설명합니다. 이 새로운 기능은 벤치마크 테스트의 예측 가능성을 높여주며, 보다 안정적인 성능 측정을 가능하게 합니다.
👉 [자세히 보기](https://go.dev/blog/testing-b-loop)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
제목: Helm @ KubeCon + CloudNativeCon EU '25

Helm 팀이 2025년 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU에 참가합니다. 올해 말 출시 예정인 Helm 4에 대해 유지보수팀과의 대화에 참여할 수 있는 기회가 주어지며, Project Pavilion에 있는 Helm 부스에서도 다양한 활동이 진행됩니다. 행사 기간 동안 모든 Helm 관련 활동에 대한 자세한 내용은 링크를 통해 확인할 수 있습니다.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

