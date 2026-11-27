"""Dong bo ma nguon notebook sach sang 03_SourceCode/notebooks/.

Script nay quet toan bo tep .ipynb trong
02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem/ (bo qua .ipynb_checkpoints/)
va sao chep giu nguyen cau truc thu muc vao
DS317_R11_Nhom03_HoSoNopDoAn/03_SourceCode/notebooks/ khi dong goi nop.
"""

# 1. Thu vien chuan
import argparse
from pathlib import Path
import shutil
import sys


def collect_notebooks(src_root: Path, dst_root: Path) -> list[tuple[Path, Path]]:
    """Thu thap danh sach cap (nguon, dich) cac notebook sach.

    Args:
        src_root (Path): Thu muc 02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem.
        dst_root (Path): Thu muc dich 03_SourceCode/notebooks.

    Returns:
        list[tuple[Path, Path]]: Danh sach cap duong dan can sao chep.
    """
    pairs: list[tuple[Path, Path]] = []
    if not src_root.is_dir():
        return pairs

    for path in sorted(src_root.rglob("*.ipynb")):
        if ".ipynb_checkpoints" in path.parts:
            continue
        rel = path.relative_to(src_root)
        pairs.append((path, dst_root / rel))
    return pairs


def run_sync(src_root: Path, dst_root: Path, dry_run: bool) -> int:
    """Thuc thi sao chep ma nguon sach hoac in ban xem truoc (--dry-run).

    Args:
        src_root (Path): Thu muc nguon chua cac notebook.
        dst_root (Path): Thu muc dich trong 03_SourceCode/.
        dry_run (bool): Neu True chi liet ke khong ghi file.

    Returns:
        int: Ma thoat (0 neu thanh cong).
    """
    if not src_root.is_dir():
        print(f"[ERROR] Khong tim thay thu muc nguon: {src_root}")
        return 1

    pairs = collect_notebooks(src_root=src_root, dst_root=dst_root)
    mode = "DRY-RUN" if dry_run else "THUC THI"
    print(f"=== DONG BO MA NGUON SACH ({mode}) ===")
    print(f"  - Nguon: {src_root}")
    print(f"  - Dich:  {dst_root}")
    print(f"  - Tong so notebook hop le: {len(pairs)}")

    for src, dst in pairs:
        size_kb = src.stat().st_size / 1024.0
        print(f"    + {src.relative_to(src_root)} ({size_kb:.1f} KB)")
        if not dry_run:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)

    if not dry_run:
        print(f"[DONE] Da sao chep {len(pairs)} notebook sang {dst_root}")
    return 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    """Phan tich tham so dong lenh.

    Args:
        argv (list[str]): Danh sach doi so dong lenh.

    Returns:
        argparse.Namespace: Doi tuong tham so da phan tich.
    """
    code_dir = Path(__file__).resolve().parent
    repo_root = code_dir.parents[1]
    default_src = repo_root / "02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem"
    default_dst = code_dir / "notebooks"

    parser = argparse.ArgumentParser(
        description=(
            "Dong bo notebook sach tu 02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem "
            "sang 03_SourceCode/notebooks/."
        )
    )
    parser.add_argument(
        "--src-root",
        type=Path,
        default=default_src,
        help="Thu muc ma nguon goc.",
    )
    parser.add_argument(
        "--dst-root",
        type=Path,
        default=default_dst,
        help="Thu muc dich trong 03_SourceCode/.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Chi liet ke danh sach file, khong ghi xuong dia.",
    )
    return parser.parse_args(argv)


def main() -> int:
    """Diem vao chinh cua script dong bo ma nguon.

    Returns:
        int: Ma thoat cua chuong trinh.
    """
    args = parse_args(sys.argv[1:])
    return run_sync(
        src_root=args.src_root,
        dst_root=args.dst_root,
        dry_run=args.dry_run,
    )


if __name__ == "__main__":
    raise SystemExit(main())
