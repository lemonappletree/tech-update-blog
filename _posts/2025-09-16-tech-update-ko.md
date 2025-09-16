# 🛠️ 2025-09-16 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.34: Decoupled Taint Manager Is Now Stable
Kubernetes v1.34 버전에서는 노드 수명 주기 관리와 파드 축출을 분리하여 각각의 컴포넌트로 관리하는 기능이 안정화되었습니다. 이전에는 노드 수명 주기 컨트롤러가 NoExecute 오염을 통해 노드를 비정상으로 표시하고 파드를 축출하는 역할을 모두 수행했습니다. 이제 전용 오염 축출 컨트롤러가 축출 과정을 관리하며, 노드 수명 주기 컨트롤러는 오염 적용에만 집중합니다. 이로 인해 코드 구조가 개선되고, 오염 기반 축출 컨트롤러를 개선하거나 사용자 정의 구현을 만드는 것이 더 쉬워졌습니다. 새로운 기능으로는 <code>SeparateTaintEvictionController</code> 기능 게이트가 GA 단계로 승격되었으며, 사용자는 <code>--controllers=-taint-eviction-controller</code> 설정을 통해 오염 기반 축출을 비활성화할 수 있습니다. 자세한 내용은 KEP 문서와 베타 발표 기사를 참조할 수 있습니다. 이 기능의 설계, 구현, 리뷰에 기여한 모든 기여자들에게 감사의 인사를 전합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/09/15/kubernetes-v1-34-decoupled-taint-manager-is-now-stable/)

## 🔹 Spring Boot - Spring Security 6.4.10 and 6.5.4 Released
Spring Security 6.4.10과 6.5.4 버전이 출시되었습니다. 두 버전 모두 4개의 버그 수정과 여러 종속성 업그레이드를 포함하고 있으며, 이번 주에 각각 Spring Boot 3.4.10 및 3.5.6과 함께 제공됩니다. 또한, 이번 릴리스에서는 CVE-2025-41248과 CVE-2025-41249에 대한 문제를 해결했습니다. 추가 정보는 Spring Security 및 Spring Framework 릴리스 공지를 참조하세요.
👉 [자세히 보기](https://spring.io/blog/2025/09/15/spring-security-6-4-10-and-6-5-4-released)

## 🔹 Docker - The Nine Rules of AI PoC Success: How to Build Demos That Actually Ship
블로그 글 "AI PoC 성공을 위한 아홉 가지 규칙: 실제로 배포되는 데모 만들기"는 AI 개념 증명(PoC)의 실패율이 95%라고 주장하는 연구가 널리 퍼지고 있지만, 이는 과장된 정보이며 실제로는 아무도 정확한 수치를 추적하고 있지 않다는 점을 지적합니다. 글에서는 오랜 경험을 통해 팀들이 AI 시스템을 구축할 때 직면하는 중요한 문제를 강조하며, 성공적인 AI PoC를 구현하기 위한 아홉 가지 규칙을 제공합니다. 이러한 규칙은 단순히 데모를 만드는 것 이상의 실제 배포로 이어지는 방법에 초점을 맞추고 있습니다.
👉 [자세히 보기](https://www.docker.com/blog/ai-poc-success-rules/)

## 🔹 Java - All API Additions From Java 21 to 25 #RoadTo25
이 블로그 글은 Java 21부터 Java 25까지의 모든 API 추가 사항을 다룹니다. 주요 추가 기능으로는 스코프 값, 스트림 수집기, 클래스 파일 API, 외부 함수 및 메모리 API, Javadoc 추가 기능 등이 있습니다. 이러한 새로운 기능들은 Java의 기능성과 효율성을 크게 향상시키는 데 기여할 것으로 기대됩니다.
👉 [자세히 보기](https://inside.java/2025/09/09/roadto25-api/)

## 🔹 Golang - A new experimental Go API for JSON
Go 1.25 버전에서는 새로운 실험적 JSON API가 도입되었습니다. 이 버전에서는 `encoding/json/jsontext`와 `encoding/json/v2` 패키지에 대한 지원이 추가되었습니다. 이러한 변경 사항은 JSON 데이터를 처리하는 Go 애플리케이션 개발자들에게 유용할 것으로 기대됩니다.
👉 [자세히 보기](https://go.dev/blog/jsonv2-exp)

## 🔹 Helm - Path To Releasing Helm v4
제목: Helm v4 출시를 위한 경로

요약: Helm v4의 첫 번째 알파 버전이 출시되었습니다. Helm v4 개발이 막바지에 이르렀으므로, 현재 진행 상황과 더 넓은 커뮤니티가 어떻게 참여할 수 있는지에 대한 세부 사항을 공유하고자 합니다.
👉 [자세히 보기](https://helm.sh/blog/path-to-helm-v4/)

