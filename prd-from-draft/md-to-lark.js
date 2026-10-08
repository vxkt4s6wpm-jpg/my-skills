#!/usr/bin/env node
/**
 * Markdown to Lark Blocks Converter
 * Convert PRD markdown to Feishu document blocks
 */

const fs = require('fs');
const marked = require('marked');

/**
 * Create heading block
 */
const createHeadingBlock = (level, text) => {
  const blockTypeMap = {
    1: 'heading1',
    2: 'heading2',
    3: 'heading3',
    4: 'heading4',
    5: 'heading5',
    6: 'heading6',
    7: 'heading7',
    8: 'heading8',
    9: 'heading9'
  };

  return {
    block_type: level,
    [blockTypeMap[level]]: {
      elements: [{ text_run: { content: text } }]
    }
  };
};

/**
 * Create table block
 */
const createTableBlock = (header, rows) => {
  const headerCells = header.map(h => ({
    elements: [{ text_run: { content: h } }]
  }));

  const rowCells = rows.map(row =>
    row.map(cell => ({
      elements: [{ text_run: { content: cell } }]
    }))
  );

  return {
    block_type: 11,
    table: {
      property: {
        row_size: rows.length + 1,
        column_size: header.length
      },
      table_cells: [headerCells, ...rowCells]
    }
  };
};

/**
 * Create text block
 */
const createTextBlock = (text) => ({
  block_type: 2,
  text: {
    elements: [{ text_run: { content: text } }]
  }
});

/**
 * Create bullet list block
 */
const createBulletBlock = (items) => ({
  block_type: 3,
  bullet: {
    elements: items.map(item => ({ text_run: { content: item } }))
  }
});

/**
 * Create ordered list block
 */
const createOrderedBlock = (items) => ({
  block_type: 4,
  ordered: {
    elements: items.map(item => ({ text_run: { content: item } }))
  }
});

/**
 * Convert markdown to Lark blocks
 */
const convertToBlocks = (markdown) => {
  const tokens = marked.lexer(markdown);
  const blocks = [];

  tokens.forEach(token => {
    switch (token.type) {
      case 'heading':
        blocks.push(createHeadingBlock(token.depth, token.text));
        break;

      case 'table':
        blocks.push(createTableBlock(token.header, token.rows));
        break;

      case 'paragraph':
        blocks.push(createTextBlock(token.text));
        break;

      case 'list':
        const items = token.items.map(item => item.text);
        if (token.ordered) {
          blocks.push(createOrderedBlock(items));
        } else {
          blocks.push(createBulletBlock(items));
        }
        break;

      case 'blockquote':
        blocks.push({
          block_type: 22,
          quote: {
            elements: [{ text_run: { content: token.text } }]
          }
        });
        break;

      case 'code':
        blocks.push({
          block_type: 15,
          code: {
            language: token.lang || 'plaintext',
            elements: [{ text_run: { content: token.text } }]
          }
        });
        break;

      // Skip images as Feishu doc blocks don't support direct image insertion
      case 'image':
        break;

      default:
        break;
    }
  });

  return blocks;
};

// Main execution
if (require.main === module) {
  const args = process.argv.slice(2);
  if (args.length === 0) {
    console.error('Usage: node md-to-lark.js <markdown_file>');
    process.exit(1);
  }

  const mdFile = args[0];
  const markdown = fs.readFileSync(mdFile, 'utf-8');
  const blocks = convertToBlocks(markdown);

  console.log(JSON.stringify(blocks, null, 2));
}

module.exports = { convertToBlocks };
