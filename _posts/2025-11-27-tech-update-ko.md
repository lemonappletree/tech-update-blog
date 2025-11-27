# 🛠️ 2025-11-27 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.35 Sneak Peek
Kubernetes v1.35의 출시가 다가옴에 따라, 몇 가지 주요 변경 사항과 향상된 기능이 소개되었습니다. cgroup v1 지원이 제거될 예정이며, 이는 오래된 Linux 배포판을 사용하는 클러스터 관리자에게 영향을 미칩니다. 또한, kube-proxy의 ipvs 모드가 더 이상 지원되지 않으며, containerd v1.y 지원도 중단됩니다. 새로운 기능으로는 노드가 지원하는 Kubernetes 기능을 명시적으로 선언할 수 있는 '노드 선언 기능' 프레임워크가 도입됩니다. 이외에도 Pod 리소스를 재시작 없이 업데이트할 수 있는 기능과, Pod 인증서를 통한 보안 강화, taints에 대한 수치 연산자 지원, 그리고 사용자 네임스페이스를 통한 보안 강화 등이 포함됩니다. 마지막으로, OCI 이미지를 볼륨으로 마운트하는 기능이 소개됩니다. 이러한 변경 사항들에 대해서는 Kubernetes 공식 블로그와 관련 문서에서 더 많은 정보를 확인할 수 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/11/26/kubernetes-v1-35-sneak-peek/)

## 🔹 Spring Boot - Spring Cloud 2025.1.0 (aka Oakwood) has been released
Spring Cloud 2025.1.0 (Oakwood) 버전이 정식으로 출시되었습니다. 각 프로젝트는 5.0.0 버전으로 업데이트되었고, Spring Framework 7 및 Spring Boot 4를 기반으로 합니다. 주요 변경 사항으로는 `spring-cloud-starter-parent` 아티팩트의 제거, Spring Cloud Gateway의 null-safety 주석 추가, JSpecify 초기 지원, Google 라이브러리를 사용한 gRPC에서의 JSON 처리 등이 있습니다. 또한, Spring Cloud Config는 Jackson 3로 전환되고, Spring Cloud Stream에서는 Reactor Kafka가 중단됨에 따라 관련 아티팩트가 제거되었습니다. 모든 변경 사항은 GitHub 프로젝트에서 확인할 수 있습니다. 피드백은 GitHub, Gitter, Stack Overflow 또는 Twitter를 통해 받을 수 있습니다. Maven과 Gradle을 사용한 시작 방법도 제공됩니다.
👉 [자세히 보기](https://spring.io/blog/2025/11/25/spring-cloud-2025-1-0-aka-oakwood-has-been-released)

## 🔹 Docker - Security that strengthens the ecosystem: Docker’s upstream approach to CVE-2025-12735
이 기술 블로그 글은 Docker의 보안 접근 방식에 대해 설명합니다. 2025년 11월 24일, Docker는 Kibana 프로젝트에서 발견된 CVE-2025-12735 취약점을 해결했습니다. 이 취약점은 Elasticsearch의 시각화 및 사용자 인터페이스 계층에서 발생하는 중요한 원격 코드 실행 취약점으로, CVSS 점수 9.8을 기록했습니다. 다른 강화된 이미지 벤더들의 이미지가 여전히 이 취약점을 포함하고 있는 동안, Docker의 보안 팀은 이를 해결했습니다.
👉 [자세히 보기](https://www.docker.com/blog/security-that-strengthens-the-ecosystem-dockers-upstream-approach-to-cve-2025-12735/)

## 🔹 Java - Quality Outreach Heads-up - JDK 26: HttpClient Supports TLS Named Groups &amp; Signature Schemes
이 기술 블로그 글은 JDK 26에 대한 정보로, HttpClient가 TLS 서명 스킴과 SSLParameters에 설정된 명명된 그룹을 지원하는 방식에 대해 설명합니다. 이는 관련 프로젝트에 정기적으로 전달되는 소통의 일환입니다.
👉 [자세히 보기](https://inside.java/2025/11/26/quality-heads-up/)

## 🔹 Golang - Go’s Sweet 16
블로그 글 "Go’s Sweet 16"은 프로그래밍 언어 Go의 16주년을 축하하는 내용입니다. 글에서는 Go 언어가 지난 16년 동안 어떻게 발전해왔는지와 그 동안의 주요 성과를 다루고 있습니다. 또한, Go 커뮤니티의 기여와 앞으로의 방향성에 대해서도 언급하고 있습니다.
👉 [자세히 보기](https://go.dev/blog/16years)

